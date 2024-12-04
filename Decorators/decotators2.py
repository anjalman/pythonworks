
def swap_dec(fn):

    def wrapper(num1,num2):

        if num1<num2:

            (num1,num2)=(num2,num1)

        return fn(num1,num2)
    
    return wrapper

def round_dec(fn):

    def wrapper(num1,num2):

        num1=round(num1) 

        num2=round(num2)

        return fn(num1,num2)
    
    return wrapper

@round_dec
@swap_dec
def add_number(num1,num2):

    return num1+num2

@round_dec
@swap_dec
def substraction(num1,num2):

    return num1-num2

@round_dec
@swap_dec
def division(num1,num2): 

    return num1/num2

print(add_number(2.6,10.4))

# print(add_number(10,2))

print(substraction(5.8,10.6))

# print(substraction(10,5))

print(division(10.4,2.6))

# print(division(2,10))

