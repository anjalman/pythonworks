

def is_amstrong(number):

    digit_count=len(str(is_amstrong))

    original=is_amstrong

    total=0

    while (number!=0):

        digit=number%10

        exponent=digit**digit_count

        total=total+exponent


        number=number//10


    print("amstrong" if total==original else "not amstrong")


print(is_amstrong(153))