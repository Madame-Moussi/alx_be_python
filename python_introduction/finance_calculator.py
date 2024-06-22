income = int(input("Enter your monthly income:"))  #user generated monthly income
expense = int(input("Enter your total monthly expense:")) #user generated monthly expense
MonthlySavings = income - expense
ProjectedSavings = (MonthlySavings * 12) + (MonthlySavings * 12 * 0.05)
print(f"Your monthly savings are {MonthlySavings}")
print(f"Projected savings after one year, with interest, is:{ProjectedSavings}")