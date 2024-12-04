
from re import fullmatch

user_input=input("enter variable name:")

# start with an alphabet(lower or upper)
# any number of alphabets,digits,_

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:

    print("valid")