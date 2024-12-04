all=open("D:\\pythonworks\\Datasets\\all_students.txt","r")

f=open("D:\\pythonworks\\Datasets\\failedstudents.txt","r")

all_students_set=set()

failed_students=set()

for line in all:

    line=line.rstrip("\n")
    all_students_set.add(line)

for line in f:

    line=line.rstrip("\n")
    
    failed_students.add(line)
passed_students=all_students_set.difference(failed_students)

print(passed_students)


failed_students=all_students_set.difference(passed_students)

print(failed_students)

all.close()
f.close()
