# dictionary methods


employee={"e_id":101,"name":"Arjun.M","department":"backend","age":23,"salary":35000}

# print(employee)

# print(employee["salary"])

print(employee.get("department"))

print("txt msg1")

print("txt msg2")

# we use the get(), if any error in line that print "none" and get next line output

# employee.pop("salary") 

# print(employee)

# fetch all keys in dictionary

for k in employee.keys():

    print(k)

    
#fetch all values in dictionary

for v in employee.values():

    print(v)

# get(key),pop(key),keys(),values()

# fetch keys and Values

for k,v in employee.items():

    print(k,v)
