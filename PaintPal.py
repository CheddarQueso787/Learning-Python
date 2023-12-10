#paintpal
#Ileana Perez Ruiz
#The purpose of this program is to calculate the total estimate for an interior home paint project. 
#I pledge that this is my own work

print ("Welcome to Paint Pal. This program will give you a price quote for painting a room.")
print ("\n Please enter each measurement in feet.")

ceilingheight = float(input("\n What is the ceiling height? "))

wall1 = float(input("\n What is the width of wall 1? "))
wall2 = float(input("\n What is the width of wall 2? "))
wall3 = float(input("\n What is the width of wall 3? "))
wall4 = float(input("\n What is the width of wall 4? "))

totalsqft = (wall1 + wall2 + wall3 + wall4) * ceilingheight
roundtotalsqft = round(totalsqft, 2)

totalpaint = (totalsqft * 48.16)/400
roundtotalpaint = round(totalpaint, 2)

overhead = 400+(totalpaint * .47)
roundoverhead = round(overhead, 2)
 
finalamount = totalpaint + overhead
roundfinalamount = round(finalamount, 2)

print("\n Your total square footage is: ",roundtotalsqft,".",sep = "")
print ("\n The total cost of paint is: $",roundtotalpaint,".",sep = "")
print ("\n The total overhead cost is: $",roundoverhead,".",sep = "")
print("\n The total price quote for this room is: $",roundfinalamount,".",sep = "")
print ("\n Thank you for using Paint Pal.")

