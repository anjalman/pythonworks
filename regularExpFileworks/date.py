from re import findall

f=open("D:\\pythonworks\\regularExpFileworks\\date.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

date=findall(pattern,content)

for d in date:

    print(d)