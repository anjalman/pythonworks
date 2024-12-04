
student_Data={

    "hari":[30,34,35],
    "vipin":[35,25,40],
    "vinay":[36,34,33],
    "vikhal":[38,45,35],
    "akshay":[37,35,38]

}
student_avg_mark={k:sum(v)/len(v)for k,v in student_Data.items()}

print(student_avg_mark)
# index=4
# for i,element in enumerate(student_Data):
    
#     if i+1==index:

#         mark=student_Data.get(element)

#         avg=sum(mark)/len(mark)

#         print(avg)

    