
# create a dictinory employeee with keys eid,name,salary,department,experience

employee={"e_id":101,"name":"Abhishek","salary":15000,"department":"electrical","experience":4}

# print(employee["e_id"])

# print(employee["name"])

# print(employee["salary"])

# print(employee["department"])

# print(employee["experience"])

employee["contact"]=6284759631
# """if experience >5 employee salary as current_salary+10000
#         else 50000"""


if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"


print(employee)

