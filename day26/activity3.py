class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name 
        self.age=age
blu=parrot("blu",10)
woo=parrot("woo",15)
print("blu is a ",blu.species)
print("woo is a ",woo.species)
print(blu.name,blu.age)
print(woo.name,woo.age)