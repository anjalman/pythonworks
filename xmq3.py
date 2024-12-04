
def is_palindrom(string:str)->bool:

    string=string.replace(" ","").lower()

    return string==string[::-1]
print(is_palindrom("racecar"))

print(is_palindrom("hello"))