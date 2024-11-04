num = int(input("Please enter a number that is greater than 10: "))

while num <= 10:
        print("The number must be greater than 10. Please try again.")
        num = int(input("Please enter a number that is greater than 10: "))

print("Thank you! You've entered a valid number:", num)
#_________________________________
number = int(input("Please enter a number: "))

#________________________________მე-3 ვერ გავიგე
num1 = input("Please just enter num: ")
num2 = input("Please just enter num: ")


result = (num1 == num2)

while result == True:
    print("Seems like you placed the same number.")
    result = False  
if not result:
    print("The numbers you entered are not the same.")
#___________________________
num4=input("Please just enter num: ")

cal = num4 % 2

if cal == 0:
    print("The number you entered is even.")
else:
    print("The number you entered is odd.")

if cal >100 :
     print("the num that you placed is more than 100")
else:
    print("the num that you enter is smaller than 100")

#__________________________________




