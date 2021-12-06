
s1=float(input())
s2=float(input())
s3=float(input())
s4=float(input())
s5=float(input())

p=float((s1+s2+s3+s4+s5)/5)
print(p)
if(p>=90):
    print("grade A")
elif(p>80):
    print("grade B")
elif(p>70):
    print("grade C")
elif(p>60):
    print("grade D")
elif(p>40):
    print("grade E")
else:
    print("grade F")
