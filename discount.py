quantity=int(input())
if(quantity>10000):
    cost=int(quantity*100)
    discount=50/100
    pay=("price to pay :", cost*discount)
else:
    cost2=int(quantity*100)
    print("pay without discount :",cost2)