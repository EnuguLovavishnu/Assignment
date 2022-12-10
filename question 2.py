dict={
    "name":"car"
}
Brand_name=input("Enter the Car Brand_name:")
Color=input("Enter the Car_color:")
x=open("mydata.txt","a")
Cars={Brand_name:Color}
print("The car are Brand-name and color:",Cars)
print("The car are Brand-name and color:",Cars,file=x)