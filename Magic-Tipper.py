#this program will calculate your total bill including tip


#read in the starting cost and tip amount
cost = float(input("How much was the bill? "))
percentage = int(input("What percentage of the bill do you want to tip? "))

#figure out the tip and total cost with the tip added in
total = cost * (1 + percentage/100)
tip = total * (percentage/100)

#round the total to 2 decimal places
roundedtotal = round(total, 2)
roundedtip = round(tip, 2)

#print the result
print("The tip amount is:", roundedtip)
print("The total amount with tip is:", roundedtotal)
