num1=int(input("enter the num1 :"))

num2=int(input("enter the num2 :"))

try:
    result=num1/num2

    print(result)


except Exception as e:

    num2=int(input("enter the num :"))

    # result=num1/num2

    print(e)

# print("database commit")

# print("file operation")



# finally:
    print("database commit")

    print("file operation")