#Ques. Input 3 number and find avg.(comma seprated input)
num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
num3 = int(input("enter third number "))
# input one or more at a time
num4,num5,num6 = (input("enter three number ").split())
avg = (num1+num2+num3)/3
print("average of first 3 number is : " + str(avg))
avg2 = (int(num4)+int(num5)+int(num6))/3
print("average of next 3 number is : " + str(avg2))
print(f"average of three number is {(num1+num2+num3)/3}") #in python 3.6
print("average of three number is {} ".format((num1+num2+num3)/3)) # in python 3
# int() : float,str--->int
# str() : float,int--->str
# float() : int,str-->float
