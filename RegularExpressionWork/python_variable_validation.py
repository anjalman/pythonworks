from re import fullmatch

user_input=input("enter variable name:")

# start with an alphabet(lower or upper)
# any number of alphabets,digits,_

pattern="[a-zA-z][a-zA-Z0-9]*"

matcher=fullmatch(pattern,user_input)

if matcher!=None:

    print("valid")

else:

    print("invalid")

