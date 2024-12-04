# do not change the alredy defined code ,so we can reduce the repitation of code SO WE USE THE DECORATORS FUNCTION
# 1-decotaror is a normal function 
# 2-()parameter takes another function eg:def swap_decotors(fn):
# 3-there is a another inner function  eg:def wrapper
# 4-parameter nte count same aavanam aaa inner function  ngte ullil eg:def wrapper(n1,n2)
# 5-
def swap_decarators(fn):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)
        
    return wrapper


@swap_decarators
def smart_sub(num1,num2):
        
        return num1-num2

@swap_decarators

def smart_div(num1,num2):

    return num1/num2

print(smart_sub(10,2))

print(smart_sub(2,10))

print(smart_div(2,10))

print(smart_div(10,2))