

text1="PQRST"

text2="ABC"

smallest_text= text1 if len(text1)<len(text2) else text2

largest_text=text1 if len(text1)>len(text2) else text2

result=""

for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]

print(result)

balance_txt=largest_text[len(smallest_text):]

result+=balance_txt

print(result)



text="ABCABC"
