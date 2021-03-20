n=int(input("enter the no to check"))
m=n
rev=0
while n>0:
    l=n%10
    rev=rev*10+l
    n=n//10
if(m==rev):
    print("palidrome")
else:
    print("not a palidrome")

