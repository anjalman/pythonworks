from re import findall

f=open("D:\\pythonworks\\regularExpFileworks\\ulr.txt")

# for line in f:

#     words=line.rstrip("\n")

#     pattern="(https|http)://[\w\S]+"

#     matcher=finditer(pattern,words)

#     for obj in matcher:

#         print(obj.group())

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)
