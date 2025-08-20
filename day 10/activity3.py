n=int(input("enter your number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit **3
    temp //=10
if n==sum:
    print("its a armstrong number")
else:
    print("its not a armstrong number")