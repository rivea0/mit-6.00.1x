"""Calculates the credit card balance after one year if
a person only pays the minimum monthly payment required by the credit card company each month.
"""

for i in range(12):
    payment = balance * monthlyPaymentRate
    unpaid_balance = balance - payment
    balance = unpaid_balance + ((annualInterestRate / 12.0) * unpaid_balance)
    # The last iteration as the 12th month
    if i == 11:
        print("Remaining balance:", round(balance, 2))