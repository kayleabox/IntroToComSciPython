'''
Assume that the interest is compounded monthly according 
to the balance at the end of the month (after the payment for that month is made). 
The monthly payment must be a multiple of $10 and is the same for all months. 
Notice that it is possible for the balance to become negative using 
this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

def pay_one_year(balance, annual_interest_rate):
  monthly_interest = annual_interest_rate/12
  lowest_pay = get_fixed_rate(10, balance, monthly_interest)
  print('Lowest Payment: ' + str(round(lowest_pay, 2)))

def get_fixed_rate(monthly_payment, balance, monthly_interest):
  remain_balance = balance

  for month in range(12):
    unpaid = remain_balance - monthly_payment 
    remain_balance = unpaid + (monthly_interest * unpaid)
    
  if(remain_balance <= 0):
    return monthly_payment
  return get_fixed_rate(monthly_payment + 10, balance, monthly_interest)

print('pay_one_year:')
pay_one_year(3329, 0.2)
print('\n')