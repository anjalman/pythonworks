
weight_in_kg=int(input("enter the weight in kg:"))

hieght_in_cm=int(input("enter your height in cm:"))

hieght_in_meter=hieght_in_cm/100

BMI=weight_in_kg/hieght_in_meter**2

round(BMI,1)

print(BMI) #21

if BMI<19: #0-18
    
    print("under weight")

elif BMI>=19 and BMI <25: #19-24
    
    print("normal weight")

elif BMI>=25 and BMI<30: #25-29

    print("over weight")

elif BMI>=30: #>30
    print("obese ")
