amount=int(input("please enter amount for withdraw"))

currency1=amount//100
currency2=(amount%100)//50
print("currency of 100 dollars ",currency1)
print("currency of 50 dollars ", currency2)