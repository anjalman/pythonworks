

weigth=int(input("enter your weight:"))

height=int(input("enter your height in cm:"))

age=int(input("enter your age:"))

gender=input("enter your gender:").lower()

print(weigth,height,age,gender)

if gender=="male":
    BMR=10*weigth+6.25*height-5*age+5

elif gender=="female":

    BMR=10*weigth+6.25*height-5*age-161

else:
    print("********please enter a valid gender******")
print(BMR)

activity_level=int(input(""""
                         
                         press 1 for sedentary active
                         press 2 for light active
                         press 3 for moderate active
                         press 4 for very active
                         press 5 for exta active
                         
"""))
if activity_level==1:
    calories=BMR*1.2

elif activity_level==2:
    calories=BMR*1.375

elif activity_level==3:
    calories=BMR*1.55


elif activity_level==4:
    calories=BMR*1.725

elif activity_level==5:
    calories=BMR*1.9

else:
    print("enter a valid activity level...")

print(f"total number of calories to need to maintain your wieght={calories}")

target_weight=int(input("enter the weigth to reduce in kg:"))

duration=int(input("enter the duration in weeks:"))

calorie_deficit=target_weight*7700

days=duration*7

daily_calorie_deficit=calorie_deficit/days

print("calorie=",daily_calorie_deficit)

