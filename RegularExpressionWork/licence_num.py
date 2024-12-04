from re import fullmatch

licence_num=input("enter the licence number :")

pattern="[A-Z]{2}[0-9]{2}[0-9]{11}"

matcher=fullmatch(pattern,licence_num)

if matcher==None:

    print("invalid")

else:

    print("valid")