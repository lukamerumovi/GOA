# for ციკლის მეშვეობით შეასრულეთ ყველა მათემატიკური ოპერაცია 0-დან 100-მდე რიცხვებზე 

# num = 0
# for i in range (1,100):
#     num = num + i
#     print(num)
#     i+= 1

# num = 0
# for i in range (1,100):
#     num = num - i
#     print(num)
#     i += 1


# მომხმარებელს შემოატანინეთ რიცხვი და შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვამდე ყველა რიცხვის ჯამი

# num1 = int(input("enter ur num :"))
# sum = 0
# for i in range(num1):
#     sum += i
# print(sum)

# მომხმარებელს შემოატანინეთ ორი რიცხვი ხოლო ამის შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვებს შორის ჯამი და ნამრავლი.

# num1 = int(input("enter ur num :"))
# num2 = int(input("enter ur num :"))

# sum = 0
# sum1 

# დაწერეთ ალგორითმი, რომელიც მომხმარებელს შეეკითხება რიცხვს. თუ რიცხვი ლუწია გაყავით ორზე, სხვა შემთხვევაში გაამრავლეთ სამზე და მიუმატეთ ერთი.

# num = int(input("enter ur num :"))
# if num %2 == 0:
#     print(num//2)
# else:
#     print(num*3 +1)


# დაწერეთ პროგრამა რომელიც ბეჭდავს ყველა რიცხვს 1-100 მდე რომელიც იყოფა 3-ზე და 5-ზე while roop მეშეობით.

# num = 1
# while num <100:
#     if  num %3 == 0 and num %5 == 0:
#         print(num)
#     num += 1


# დაიწყეთ 10-დან და დაითვალეთ 1-მდე, დაბეჭდეთ თითოეული რიცხვი.

# i = 10
# while i >1:
#     print(i)
#     i -= 1

# განუწყვეტლივ სთხოვეთ მომხმარებელს მისი სახელი, სანამ არ შეიყვანს "quit"-ს.

# num = input("enter ur name :")
# if num == "quit" :
#     print("nice")
# else:
#     print(input("enter ur name :"))

# ამობეჭდეთ ყველა ლუწი რიცხვი 10-დან 20-მდე while ციკლის გამოყენებით.
# i = 10
# while i <20:
#     i %2 == 0
#     print(i)
#     i += 2

# მომხმარებელს შეაყვანინეთ რიცხვი და განაგრძეთ კითხვა მანამ, სანამ არ შეიტანს დადებით რიცხვს.
# num = int(input("enter number :"))
# if num <0:
#     print(int(input("enter number :")))
# else:
#     print(" good job:)")

# 1-იდან 10-ის ჩათვლით არსებული ყველა რიცხვის კვადრატი გამოიტანეთ while ციკლის გამოყენებით.
# i = 1
# while i <11:
#     print(i ** 2)
#     i += 1


# შექმენით სია რომელშიც გექნებათ 1 დან 20-მდე რიცხვები დაბეჭდეთ თითოეული სიის ელემენტი და თითოეულ მათგანს მიუწერეთ ლუწია თუ კენტი, გამოიყენეთ for loop
# for i in range(1,20):
#     if i %2 == 0:
#         print("this num is even")
#     else:
#         print("this num is odd")


# შექმენით სია რომელშიც გექნებათ 1 დან 20მდე რიცხვები შემდეგ კი დაბეჭდეთ 3 ის ჯერადი რიცხვები
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in list:
#     if i %3 == 0:
#         print(i)

# შექმენით სია რომელშიც გექნებათ ათიცალი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ ამ სიიდან მხოლოდ 10ზე დაბალი რიცხვები გამოიყენეთ for loop

# list = [1,2,3,6,11,16,4,29,20,8]
# for i in list:
#     if i <10:
#         print(i)

# შექმენით სია რომელშიც გექნებათ ოცი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ მხოლოდ 10-ზე ნაკლები და მხოლოდ ლუწი რიცხვები, ისე რომ ლუწიც იყოს და 10-ზე ნაკლებიც, გამოიყენეთ for loop

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in list:
#     if i <10 and i %2 == 0:
#         print(i)

# შექმენით სია რომელშიც გექნებათ ოცი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ მხოლოდ 20 ზე მეტი რიცხვები ისე რომ იყოს თან სამის ჯერადი გამოიყენეთ for loop
# list = [1,2,3,4,5,16,20,15,23,35,65,43,97,0,9,54,67,101,135,165,100]
# for i in list:
#     if i >20 and i %3 == 0:
#         print(i)

# შექმენით სია სადაც მოათავსებთ ხუთ სხვადასხვა სახელს შემდეგ კი მიწვდით თითოეულ ელემენტს(სახელს) და დაბეჭდეთ თითოეულში ასოების რაოდენობა, გამოგადგებათ for loop და len ფუნქცია 
# !!!!!


# შექმენით სია სადაც მოათავსებთ ხუთ სხვადასხვა სახელს შემდეგ კი დაბეჭდეთ ამ სიაში თითოეული ელემენტის პირველი ასო მხოლოდ გამოიყენეთ for loop

# name_list = ["vato", "gigi", "giorgi", "nika", "irakli"]
# for i in name_list:
#     print(i[0])