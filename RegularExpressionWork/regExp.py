
from re import finditer

text="I have 3 cars,2 bikes,1 Cycle"

# pattern="\w"    "[a-zA-Z0-9]" to get  alphanumeric

# pattern="\d" to get digits

# pattern="\D" #"[^0-9]" to exclude digits

# pattern="\W" #"[^a-zA-Z0-9]" to get speacial characters

# pattern="\s"  #to get white space

pattern="\S"  #to exclude  white space

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())