n=int(input("Enter the number to reverse"))
rev=0
while n>0:
    l=n%10
    rev=rev*10+l
    n=n//10
print(rev)