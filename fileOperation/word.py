
word_path="D:\\pythonworks\\Datasets\\word.txt"
palindrom_path="D:\\pythonworks\\fileOperation\\palindrom.txt"

f_read=open(word_path,"r")

f_write=open(palindrom_path,"w")

for line in f_read:
    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:

        f_write.write(word+"\n")

f_read.close()
f_write.close()


