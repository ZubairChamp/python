class vehicle:
    def __init__(self,maxspeed,modelname):
        self.maxspeed=maxspeed
        self.modelname=modelname
model1=vehicle(240,"tmwx5")
print("maxspeed is ",model1.maxspeed)
print("modelname is ",model1.modelname)
model2=vehicle(190,"BMW M5 CS")
print("maxspeed of my favourite car is ",model2.maxspeed)
print("modelname of my favourite car is ",model2.modelname)