coffee = float(input("What should the price of coffee be set at?: $"))

pastry = float(input("What should the price of a pastry be set at?: $"))

juice = float(input("What should the price of juice be set at?: $"))

print("Note: The set service tax is set at 10%")

total = coffee + pastry + juice

tax = total * .10

tax_total = total + tax

print("The total is $", tax_total)




