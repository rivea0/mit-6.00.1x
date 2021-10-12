"""Finds the smallest monthly payment to the cent such that we can pay off the debt within a year.
Uses lower and upper bounds and bisection search.
"""

lower = balance / 12
upper = (balance * (1 + (annualInterestRate / 12.0)) ** 12) / 12.0
mid = (lower + upper) / 2.0
initial_balance = balance
i = 0
epsilon = 0.01

while i <= 12:
    unpaid_balance = balance - mid
    balance = unpaid_balance + ((annualInterestRate / 12.0) * unpaid_balance)
    
    i += 1
    
    if i == 12 and balance < -epsilon:
        balance = initial_balance
        upper = mid
        mid = (lower + upper) / 2.0
        i = 0
    elif i == 12 and balance > epsilon:
        balance = initial_balance
        lower = mid
        mid = (lower + upper) / 2.0
        i = 0
      
print("Lowest payment:", round(mid, 2))