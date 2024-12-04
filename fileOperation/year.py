
# 1800-2024

year_path="D:\\pythonworks\\Datasets\\year.txt"

leap_year_path="D:\\pythonworks\\Datasets\\leap_year.txt"

centuary_path="D:\\pythonworks\\Datasets\\centuary_year.txt"

f_year=open(year_path,"r")

leap_year=open(leap_year_path,"w")

c_year=open(centuary_path,"w")

def is_centuary_year(year):

    return (year%100==0)

def is_leap_year(year):

    return(year%100==0 and year%400==0) or (year!=0 and year%4==0)



for year in f_year:

    year=int(year)

    if is_centuary_year(year):

        c_year.write(str(year)+"\n")

    if is_leap_year(year):

        leap_year.write(str(year)+"\n")


f_year.close()
leap_year.close()
c_year.close()