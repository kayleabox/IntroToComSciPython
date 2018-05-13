def pay_one_year_bi(balance, annual_interest_rate):
  monthly_interest = annual_interest_rate/12
  upper_bound = (balance * (1 + monthly_interest)**12) /12.0
  lower_bound = balance / 12
  lowest_pay = get_fixed_rate(balance, monthly_interest, upper_bound, lower_bound)
  print('Lowest Payment: ' + str(round(lowest_pay, 2)))

def get_fixed_rate(balance, monthly_interest, upper_bound, lower_bound):
  monthly_payment = round(lower_bound + (upper_bound - lower_bound)/2, 4)
  remain_balance = check_monthly_payment(balance, monthly_interest, monthly_payment)
  if(remain_balance <= 0 and remain_balance >= -0.01):
    return monthly_payment
  elif remain_balance < -0.01:
    upper_bound = monthly_payment
    monthly_payment = round(lower_bound + (upper_bound - lower_bound)/2, 4)
  elif remain_balance > 0: 
    lower_bound = monthly_payment
    monthly_payment = round(lower_bound + (upper_bound - lower_bound)/2, 4)
  return get_fixed_rate(balance, monthly_interest, upper_bound, lower_bound)

def check_monthly_payment(balance, monthly_interest, monthly_payment):
  remain_balance = balance
  for month in range(12):
    unpaid = remain_balance - monthly_payment 
    remain_balance = unpaid + (monthly_interest * unpaid)
  return remain_balance