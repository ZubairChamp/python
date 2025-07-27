height=float(input("enter your height in centimeters "))
weight=float(input("enter your weight in KG "))
BMI=weight/(height/100)**2
print("your BMI is ",BMI)
if BMI <= 18.4:
    print("you are under weight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are over weight")
else:
    print("you are obese")