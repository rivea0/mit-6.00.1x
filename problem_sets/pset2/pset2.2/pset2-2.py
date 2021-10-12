"""Calculates the minimum fixed monthly payment needed 
in order to pay off a credit card balance within 12 months.
"""

initial_balance = balance

# As the first payment
payment = 10

i = 0

while i <= 12:
    unpaid_balance = balance - payment
    balance = unpaid_balance + ((annualInterestRate / 12.0) * unpaid_balance)
    i += 1
    
    if i == 12 and balance > 0:
        balance = initial_balance
        payment += 10
        i = 0
        
print("Lowest payment:", payment)