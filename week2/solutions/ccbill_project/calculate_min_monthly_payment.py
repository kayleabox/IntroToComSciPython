'''
Assignment: 
For each month, calculate statements on the monthly payment and remaining balance.
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy - so print
Remaining balance: 813.41

So your program only prints out one thing: the remaining 
balance at the end of the year in the format:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest
rate x Monthly unpaid balance)
'''
def calculate_min_monthly_payment(balance, annual_interest_rate, monthly_payment_rate):
  monthly_interest = annual_interest_rate / 12
  remaining_balance =  balance

  for month in range(12):
    minimun_payment = monthly_payment_rate * remaining_balance
    unpaid = remaining_balance - minimun_payment 
    remaining_balance = unpaid + (monthly_interest * unpaid)
    
  print('Remaining balance: ' + str(round(remaining_balance, 2)))

print('Calculate Minimum Monthly Payment:')
calculate_min_monthly_payment(484, 0.2, 0.04)
print('\n')
