actual_cost=float(input("please enter the actual product price "))
sale_amount=float(input("please the sale amount "))
if(sale_amount>actual_cost):
    amount= sale_amount-actual_cost
    print("profit of ",amount)
else:
    print("no profit ")