import io
import os
import sys
import unittest
import unittest.mock

from solutions.ccbill_project.calculate_min_monthly_payment import calculate_min_monthly_payment
from solutions.ccbill_project.pay_one_year import pay_one_year
from solutions.ccbill_project.pay_one_year_bisection_search import pay_one_year_bisection_search

'''
Test Case 1:
  balance = 42
	annualInterestRate = 0.2 
  monthlyPaymentRate = 0.04
	      
Result Your Code Should Generate Below:
	Remaining balance: 31.38

Test Case 2:
	balance = 484
  annualInterestRate = 0.2
	monthlyPaymentRate = 0.04
	      
Result Your Code Should Generate Below:
  Remaining balance: 361.61
'''

class CalMinimumPaymentTest(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, balance, annual_interest_rate, monthly_payment_rate, expected_output, mock_stdout):
    calculate_min_monthly_payment(balance, annual_interest_rate, monthly_payment_rate)
    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    self.assert_stdout(484, 0.2, 0.04, 'Remaining balance: 361.61')
    self.assert_stdout(42, 0.2, 0.04, 'Remaining balance: 31.38')


'''
Test Case 1:
	balance = 3329
	annualInterestRate = 0.2

Result Your Code Should Generate:
	Lowest Payment: 310
                
Test Case 2:
  balance = 4773
	annualInterestRate = 0.2
	      
Result Your Code Should Generate:
	Lowest Payment: 440

Test Case 3:
  balance = 3926
	annualInterestRate = 0.2

Result Your Code Should Generate:
	Lowest Payment: 360
'''

class CalPayOneYearTest(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, balance, annual_interest_rate, expected_output, mock_stdout):
    pay_one_year(balance, annual_interest_rate)
    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    self.assert_stdout(3329, 0.2, 'Lowest Payment: 310')
    self.assert_stdout(4773, 0.2, 'Lowest Payment: 440')
    self.assert_stdout(3926, 0.2, 'Lowest Payment: 360')


'''
Test Case 1:
	balance = 320000
	annualInterestRate = 0.2

Result Your Code Should Generate:
	Lowest Payment: 29157.09

Test Case 2:
	balance = 999999
	annualInterestRate = 0.18
	      
Result Your Code Should Generate:
	Lowest Payment: 90325.03  
'''

class CalPayOneYearBisectionTest(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, balance, annual_interest_rate, expected_output, mock_stdout):
    pay_one_year_bisection_search(balance, annual_interest_rate)
    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    self.assert_stdout(320000, 0.2, 'Lowest Payment: 29157.09')
    self.assert_stdout(999999, 0.18, 'Lowest Payment: 90325.03')
