class vehicle:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
class bus(vehicle):
    pass
schoolbus=bus("volvo bus",180,12)
print("vehicle name ",schoolbus.name," speed :",schoolbus.speed," mileage: ",schoolbus.mileage)