

colors=["red","green","blue"]

#colors.append()#insert  new object end of the list

colors.append("yellow")

print(colors)

# colors.pop() to remove the last object and return it

poped_elmnt=colors.pop()

print(colors)

# colors.insert() to add an elemnt in the middle

colors.insert(0,"purple")

print(colors)

# red_index=colors.index("red") its return the index number of red

red_index=colors.index("red")

print(red_index)

# copy to copy the elemnt

binus_fvt_clr=['black','blue','skyblue','white']

kunjus_fvt_clr=binus_fvt_clr.copy()

kunjus_fvt_clr.pop()

print("bk",binus_fvt_clr)

print("ku",kunjus_fvt_clr)


# copy()
# index("object")
# insert()
# pop()
# append()

# sort( reverse=false) to sort the array


lst=[2,6,3,8,5,4]

lst.sort()

lst.sort(reverse=True)

print(lst)





