
unit= float(input())
if(unit<50):
    print("total bill to pay :",unit*0.50 + unit*0.50*.2 )
elif(50<=unit<150):
    print("total bill to pay :",unit*0.75 + unit*0.75*.2)
elif(150<=unit<250):
    print("total bill to pay :",unit*1.20 + unit*1.20*.2)
else:
    print("total bill to pay :",unit*1.50 + unit*1.50*.2)