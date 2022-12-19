import pandas as pd
s1=[]
s2=[]
number=int(input("enter the number:"))
for i in range(0,number):
    m=int(input("Enter the number:"))
    s1.append(m)
    square=pd.Series((m**2))
    s2.append(m**2)
    value=pd.Series(s2,index=[s1])
    print(value)