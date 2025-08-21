text=input("enter your own word: ")
char=input("please enter your own character")
i=0
count=0
while(i<len(text)):
    if(text [i]==char):
        count=count+1
    i=i+1
print("your search character occures: ",count)