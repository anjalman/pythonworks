
from re import fullmatch

adhaaar_num=input("enter the adhaar number :")

pattern="[0-9]{4}[0-9]{4}[0-9]{4}"

matcher=fullmatch(pattern,adhaaar_num)

if matcher==None:

    print("invalid")

else:

    print("valid")

