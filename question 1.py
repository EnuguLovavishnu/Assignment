User_1=int(input("Enter the First User input:"))
User_2=int(input("Enter the Second User input:"))
User_3=int(input("Enter the Third User input:"))
User_4=int(input("Enter the Four User input:"))
User_5=int(input("Enter the Five User input:"))
# using the list
num=[User_1,User_2,User_3,User_4,User_5]
# using the loops
for i in num:
    print(i)

#using if-else statememts
if((User_1>=0) and (User_2>=0) and (User_3>=0) and (User_4>=0) and(User_5>=0)):
    x=open("mydata.txt","a")
    print("The positive numbers")
    print("The positive numbers",file=x)
else:
    x=open("mydata.txt","a")
    print("The negative numbers")
    print("The negative numbers",file=x)


x=open("mydata.txt","a")
total=(User_1+User_2+User_3+User_4+User_5)
print("Adding the positive numbers:",total)
print("Adding the positive numbers:",total,file=x)



