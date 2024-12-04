
from re import finditer

text="abbbababbabaaaab"

# pattern="a{2}" #to get double "a" index in the text

pattern="a{1,3}" #to get minimum 1a and maximum 3a

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())

