

f=open("D:\\pythonworks\\Datasets\\fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)