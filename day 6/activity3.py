print("enter marks obtained in 5 subjects")
num1=int(input("marks 1"))
num2=int(input("marks 2"))
num3=int(input("marks 3"))
num4=int(input("marks 4"))
num5=int(input("marks 5"))
total=num1=num2+num3+num4+num5
average=total/5
if average >= 91 and average <= 100:
    print("grade a1")
elif average >= 81 and average < 91:
    print("grade a2")
elif average>= 71 and average < 81:
    print("grade b1")
elif average>= 61 and average < 71:
    print("grade b2")
elif average > 30 and average < 61:
    print("grade c1")
else:
    print("grade e1")