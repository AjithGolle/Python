# compound interest program
import math

principal = 0
rate = 0
time = 0

while principal <= 0  :
    principal = float(input("enter the principal amount :"))
    if principal <=0 :
        print("principal amount cant be less than or equals to zero !")

while rate <=0 :
    rate = float(input("enter the interest rate :"))
    if rate <= 0 :
        print("interest rate cant be less than or equal to zero !")

while time <=0 :
    time = int(input("enter the time in years :"))
    if time <=0 :
        print("time cant be less than or equals to zero !")

print(principal)
print(rate)
print(time)

total = principal * (pow((1 + rate/100), time))
print("the total amount is :",total)