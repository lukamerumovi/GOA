# 0 დან 20 ჩათვლით ვპრინტავთ მთელ რიცხვებს

# for i in range(0, 21):
#     print(i)

# ვპრინტავთ პირველ 10 ნატურალურ რიცხვს

# for i in range(0,10):
#     print(i)

# ვპრინტავთ 1 დან 100 მდე ლუწ რიცხვებს

# for i in range(0, 101):
#      if i %2 == 0:
#           print(str(i))

# დაწერეთ პროგრამა, რომელიც გამოთვლის და ბეჭდავს რიცხვების ჯამს 1-დან 10-მდე floop is გამოყენებით
# !!211111111
# num1 = 0
# for i in range(1, 11):
#     num1 = num1 + i
#     print(num1)

# ამობეჭდეთ რიცხვების კვადრატები 1-დან 15-მდე.

# for i in range(1, 15):
#     num1 = i * i
#     print(num1)

# for i in range(1, 16):
#     print(i * i)

# დაწერეთ პროგრამა, რომელიც გამოითვლის და დაბეჭდავს 1-დან 5-მდე რიცხვების კვადრატების ჯამს

# for i in range(1,5):
#     num1 = i * i 
# print(num1)


# დაბეჭდეთ რიცხვები, რომლებიც იყოფა 3-ზე და 5-ზე 1-დან 100-ის ჩათვლით

# for i in range(1,101):
#     if i %3 == 0 or i  %5 == 0:
#         print(i)


# დაწერეთ პროგრამა, რომელიც ბეჭდავს ციფრებს 10-დან 1-მდე საპირისპირო თანმიმდევრობით 

# for i in range(10, 0, -1 ):
#     print(i)


# შემოატანინეთ მომხმარებელს რიცხვი და დაადგინეთ არის თუ არა დადებითი უარყოფითი ან ნულის ტოლი 

# num1 = int(input("enter a number"))
# if num1 >0:
#     print("the number is positive")
# elif num1 <0:
#     print("the number is negative")
# else:
#     num1 == 0
#     print("the num equal to zero")



# შემოატანინეთ მომხმარებელს მისი ასაკი თუ მისი ასაკი 18 წელზე მეტია დაუპრინტეთ “you are adult” თუ 18 წელზე ნაკლები “you are virgin”

# num1 = int(input("enter ur num :"))
# if num1 >= 18:
#     print("you are adult")
# else:
#     print("you are virgin")
    
# დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს მომხმარებლის შემოტანილი რიცხვის მიხედვით (1 არის ორშაბათი, 2 სამშაბათი და ა.შ) გამოიყენეთ if elif else 

# num1 = int(input("enter a number :"))
# if num1 == 1:
#     print("ორშაბათი")
# elif num1 == 2:
#     print("სამშაბათი")
# elif num1 == 3:
#     print("ოთხშაბათი")
# elif num1 == 4:
#     print("ხუთშაბათი")
# elif num1 == 5:
#     print("პარასკევი")
# elif num1 == 6:
#     print("შაბათი")
# elif num1 == 7:
#     print("კვირა")
