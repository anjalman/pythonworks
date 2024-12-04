

# string "sequance of characters"

# string=> object class

# class str:(design,templates)
 
# text="helloPython"

# print(text.isalpha())

# print(text.capitalize())

# print(text.isnumeric())

# print(text.endswith("on"))

# print(text.startswith("he"))

# print(text.casefold())

# print(text.isdigit())

# print(text.isalnum())


# for ch in text:

#     print(ch)



# string.split()


text="hello,python,world"

word=text.split(",")
print(word)



text="\n  this is a line \n"

# remove \n(to remove LandR both sides use strip() function)

new_text=text.strip("\n")
print(new_text)

# text.lstrip()
# text.rstrip()


# to replace

text="hello world program"

# o=>a

new_text=text.replace("o","a",)
print(new_text)


# to slice the word

text="python programming"

    # 012345678901234567
    # string_object[start:end:step]

print(text[0:6])

# out=python

print(text[:18])

# out=python programming

print(text[::2])

# out=pto rgamn

print(text[::-1])

# out=gnimmargorp nohtyp(entire string will be reversed (-1))

text="hello"

reversed_text=text[::-1]
print(reversed_text)