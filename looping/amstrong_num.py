


number=int(input("enter the number:"))  #153

digit_count=len(str(number))  #3

original=number

total=0


while(number!=0):  #153!=0.

    digit=number%10  #153%10=3

    exponent=digit**digit_count #3**3=27

    total=total+exponent  #0+27=27

    number=number//10 #153//10=15


print("amstrong number"if total==original else"not amstrong")


# num=int(input("enter num:"))
# digit_count=len(str(num))
# original=num
# total=0