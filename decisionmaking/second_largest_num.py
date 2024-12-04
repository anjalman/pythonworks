num1=int(input("enter first numbr:"))
num2=int(input("enter  second number:"))
num3=int(input("enter third number:"))

if num1>num2 and num1>num3:
    if num2>num3:
        print(f"{num2} is second largest number..")
    else:
        print(f"{num3} is the second largest number..")

elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"{num1} is the second largest number..")

    else:
        print(f"{num3} is the second largest number..")

elif num3>num1 and num3>num2:
    if num2>num1:
        print(f"{num2} is the second largest number..")

    else:
        print(f"{num1} is the seconmd largest. ")
elif num1==num2 and num2==num3:

    print("ita equal")

