
#Given two integer numbers return their sum. If the sum is greater than 100, then return their product.

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a==b==c==d):
    summ = a+b
    if(summ>100):
        p=a*b
        print("product is ",p)
else:
    print("values are not equal)