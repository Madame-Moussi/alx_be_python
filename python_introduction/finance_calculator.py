monthly_income = int(input("Enter your monthly income:"))  #user generated monthly income
monthly_expenses = int(input("Enter your total monthly expense:")) #user generated monthly expense
monthly_savings = monthly_income - monthly_expenses
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is:{projected_savings}")