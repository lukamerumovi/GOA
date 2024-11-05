num1 = int(input("enter ur num: "))
if num1 < 10: 
    print(num1, "< 10")
else:
    print(num1, "> 10")

num1 = int(input("enter ur num: "))
if num1 % 2 == 0: 
    print(f"{num1} even")
else:
    print(f"{num1} odd")

num1 = int(input("enter ur num: "))
if num1 < 0:
    print(f"{num1} is not positive")
else:
    print(f"{num1} is positive")

num1 = int(input("enter ur num: "))
num2 = int(input("enter ur num: "))

if num1 == num2:
    print(f"{num1} = {num2}" )
else:
    print(f"{num1} != {num2}" )

num1 = int(input("enter ur num: "))
if num1 > 100 and num1 % 2 == 0 : 
    print(f"{num1} is > 100 and even ")
else:
    print(f"{num1} is not > 100 and is not even ")

num1 = int(input("enter ur num"))
if num1 % 5 == 0 or num1 % 10 == 0:
    print(f"{num1} aris 5 an 10 jeradi")
else:
    print(f"{num1} ar aris 5 an 10 jeradi")

num1 = int(input("enter ur num"))
if num1 < 0:
    print(f"is < 0")
else:
    print(f"is not < 0")

number = input("Enter Num: ")

if number.isdigit() or (number.startswith('-') and number[1:].isdigit()):
    print(f"{number} is integer")
else:
    print(f"{number} float")

age = int(input("enter ur age: "))
if age >= 18:
    print("u are adult")
else:
    print("u are kid")
    
num1 = int(input("Enter ur num: "))

if num1 % 2 == 0 or num1 % 3 == 0:
    print(f"{num1} aris luwi an 3-is jeradi")
else:
    print(f"{num1} arc luwi da arc 3-is jeradia")

num1 = int(input("enter ur num: "))
if num1 == 0 or num1 == 1:
    print("num is correct")
else:
    print("num is incorrect")

num1 = int(input("Enter ur num1: "))
num2 = int(input("Enter ur num2: "))

if num1 > num2 and num1 % 10 == 0:
    print(f"{num1} aris 10-is jeradi da {num2}-ze metia")
elif num2 > num1 and num2 % 10 == 0:
    print(f"{num2} aris 10-is jeradi da {num1}-ze metia")
else:
    print("ert erti ticxvi ar aris 10-is jerdi")


num1 = int(input("enter ur num"))
if num1 < 0 or num1 % 2 == 0:
    print(f"{num1} aris uaryofiti an luwi")
else:
    print(f"{num1} arc luwi da arc uaryofiti")


num1 = int(input("enter ur num"))
if num1 > 0 and num1 % 20 == 0:
    print(f"{num1} aris dadebiti da 20is jeradi")
else:
    print(f"{num1} ar aris dadebiti da/an 20is jeradi ")


num1 = int(input("enter ur num"))
if num1 < 50 and num1 % 10 == 0:
    print(f"{num1} aris 50 naklebi da 10 jeradi")
else:
    print(f"{num1} ar aris 50 naklebi da/an 10 jeradi")
