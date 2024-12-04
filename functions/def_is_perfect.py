


def is_perfect (num):

    total=0

    for i in range(1,num):

        if num%i==0:
            
            total=total+i


    print("perfect" if num==total else "not pefect")

print(is_perfect(30))

print(is_perfect(28))