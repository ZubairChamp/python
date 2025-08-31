def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiplied(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
print("please select the operation: ")
print("a. Add")
print("b. subtract")
print("c. multiplied")
print("d. divide")
choice=input("please enter ur choice a/b/c/d ")
num1=int(input("enter ur 1st number: "))
num2=int(input("enter ur 2nd number: "))
if choice=="a":
    add(num1,num2)
elif choice=="b":
    subtract(num1,num2)
elif choice=="c":
    multiplied(num1,num2)
elif choice=="d":
    divide(num1,num2)
else:
    print("enter valid input")