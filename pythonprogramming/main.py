# print n number fibonacci series as per user input of n
def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b


num = int(input("Enter n to get n number fibonacci series: "))
fibo(num)


# Control flow statements

# problem statement:Write a program to calculate the electricity bill(take number of units from user)
# units and price
# first 100 units - no charge
# next 100 units - rs 5 per unit
# next 200 units rs 10 per unit
# for example if input unit is 350 then total bill amount = 2000
"""
Approach - 
1.between 100 and 200 we will charge first 100 as zero and remaining with 5 hence it would be (units -100)
  which will be used to calculate the total charge.
2. for unit > 200 then we will charge first hundred as 0 next hundred would become 100*5 = 500 then we will be left 
with (units - 200)
"""
units = int(input("Enter number of units consumed: "))
charge = 0
if units <= 100:
    charge = 0
elif 100 < units <= 200:
    charge = (units-100)*5
elif units > 200:
    charge = 500 + (units-200)*10

print("Total amount to pay: ", charge)

