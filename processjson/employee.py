
from json import load

f=open("D:\\pythonworks\\Datasets\\employee.json")

data=load(f)

for emp in data:

    print(emp) 