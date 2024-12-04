from re import finditer

f=open("D:\\pythonworks\\regularExpFileworks\\hashtag_fetch.txt")

for line in f:

    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())

# f=open("")

# for line in f:
#     words=line.rstrip("\n")
#     pattern="#\w+"
#     matcher=finditer(pattern,words)
#     for obj in matcher:
#         print(obj.group())