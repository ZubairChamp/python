list=[1,5,300000,6,7,6,7]
print("original list: ",list)
count=0
for i in list:
    count=count+i 
average=count/len(list)
print("sum= ",count)
print("average ",average)
list.sort()
print("smallest element is ",list[0])
print("largest element is ",list[-1])