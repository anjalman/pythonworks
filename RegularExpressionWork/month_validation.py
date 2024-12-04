
from re import fullmatch

month=input("enter the month :")

pattern="(0?[1-9]|1[0-2])"

matcher=fullmatch(pattern,month)

if month==None:

    print("invalid")

else:

    print("valid")