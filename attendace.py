
attendace = int(input("Enter your attendance :"))
classes= int(input("classes held :"))

p=attendace/classes*100

if(p<80):
    print("student will not be able to sit in the exmas \n percentage :" ,p,"%")
else :
    print(" student is allowed \n percetage :",p,"%")