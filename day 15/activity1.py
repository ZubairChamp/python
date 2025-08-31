def tip_amount(bill,tip_percentage):
    total=bill*(1+0.01*tip_percentage)
    total=round(total,2)
    print(f"please pay ${total}")
tip_amount(150,10)


