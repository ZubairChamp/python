def flipflop(r):
    e=len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s=s+1
        e=e-1
    return True
r=(6,7,6,7)
if(flipflop(r)):
    print("the tuple is 6,7,6,7")
else:
    print("the tuple is not 6,7,6,7")