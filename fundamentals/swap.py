num1=100

num2=200

print(f"before swap num1={num1} and num2={num2}")

# num1,num2=num2,num1 (this working on in python only )(method number 1)

# temp=num1

# num1=num2

# num2=num1 (method number 2)

num1=num1+num2 #num1=100+200=300
num2=num1-num2 #num2=300-200=100
num1=num1-num2 #num1=300-200=100

#(method number 3)


print(f"after swap num1= {num1} and num2={num2}")

