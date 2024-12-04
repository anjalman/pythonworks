
from re import fullmatch

reg_num=input("enter the vehicle number :")

# condition

# starting wiht KL

# 2 digit

# alphabets minimun1 maximum2

# 4 digit

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matchers=fullmatch(pattern,reg_num)

if matchers!=None:

        print("valid")

else:

        print("invalid")



# passport
# aadhar
# driving licence