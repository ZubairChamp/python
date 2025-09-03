valid=False
while not valid:
    try:
        n=int(input("enter a number,if u give even number it will print bye infinite times"))
        while n%2==0:
            print("bye")
        valid=True
    except ValueError as ex:
        print(ex)