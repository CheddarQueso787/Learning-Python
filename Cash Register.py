#Cash Register
#The purpose of this program is to calculate the total amount for
#each individual concession order at PTA fundraisers.
#Customers may purchase bags of popcorn $0.25, water $0.50, soda $0.75, and candy bars $1.00.


#create a variable to store the sale price of each item
popcornprice = .25
waterprice = .50
sodaprice = .75
candybarprice = 1.00

#welcome the user.
print("Welcome! \nThis program will help you calculate the total amount for each purchase. \nPlease enter the quantity you would like for each item.") 

#request the user enter and confirm each item they would like to purchase.
#create a variable to store each response. 

numwater = int(input("\n" "How many bottles of water would you like to purchase? "))
print ("\n" "You are purchasing",numwater,"bottles of water. ")

numsoda = int(input("\n" "How many cans of soda would you like to purchase? "))
print ("\n" "You are purchasing",numsoda,"cans of soda. ")

numcandy = int(input("\n" "How many candy bars would you like to purchase? "))
print ("\n" "You are purchasing",numcandy,"candy bars. ")

numpopcorn = int(input("\n" "How many bags of popcorn would you like to purchase? "))
print ("\n" "You are purchasing",numpopcorn,"bags of popcorn. ") 

#calculate the total price for all items requested.

purchasetotal = float((numwater * waterprice) + (numcandy * candybarprice) + (numsoda * sodaprice) + (numpopcorn * popcornprice))

print ("\n" "The total is $",purchasetotal,".", sep="")

amttender = float(input("\nCustomer amount tendered? "))

chngdue = float(amttender - purchasetotal)

print ("\n" "Your customer's change is ",chngdue,".", sep="")

