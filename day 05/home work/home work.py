

birth_year=int(input("please enter your birth year : "))
curent_year=2024
age=curent_year - birth_year
print("you are " + str(age) ) 
 
 


width=float(input("PLease enter  width of square : "))
length=float(input("please enter length of square : "))
area=width*length
jtcnt=width+length
perimeter=2*jtcnt
print("your squares area is : " + str(area))
print("your squares perimeter is : " + str(perimeter))




km=float(input("please enter length of your home to your school in km : "))
m=km*1000
cm=m*100
mm=cm*10
print("______________________________________________")
print(f"{m} metre is between your school and home and there is in cm {cm} and in mm is {mm} ")



name = input("Enter your first name: ")
surname = input("Enter your last name: ")
parent_name = input("Enter your parent's first name: ")
parent_surname= input("Enter your parent's last name: ")
favorite_color = input("Enter your favorite color: ")
favorite_car = input("Enter your favorite car: ")
hobby1 =input("Enter your first favorite hobby: ")
hobby2= input("Enter your second favorite hobby: ")
hobby3= input("Enter your third favorite hobby: ")

print(f"{name} {surname} is the child of {parent_name} {parent_surname}. Their favorite color is {favorite_color}, they love the {favorite_car}, and they enjoy {hobby1}, {hobby2}, and {hobby3}.")



#აქ ცოტა ტვინი შემეჭამა მაგრამ რო მივხვდი მერე გაასწორა

print("________________________________________________")
the_input=int(input("please enter two digit number : "))

first_num=the_input//10
second_num=the_input%10

print(f"the number that you chosed has {first_num} at  first num and {second_num} at second num ")
print(f"and the ")