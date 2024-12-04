

num=int(input("enter the number"))  #123
 
total=0

while(num!=0): #123!=0  12!=0   1!=0 0!=0=false lopp exit

    digit=num%10  #123%10 = 3  12%10=2  1%10=1

    digit_square=digit**2 #3**2=9      2**2=4 1**2=1


    total=total+digit_square  #0+6=6  6+4=10 10+1=11

    num=num//10 # 123//10=12  12/10=1 1//10=0

print(total)