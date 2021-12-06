income=float(input("Enter salary :"))
if(income<100000):
    print("tax will be : Rs. 00")
elif(100000<=income<200000):
    print("tax will be :",income*0.1)
else:
    print("tax will be :", income*.2)

