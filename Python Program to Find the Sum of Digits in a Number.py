n=int(input("Enter the number"))
t=0
while(n>0):
    dig=n%10
    t=t+dig
    n=n//10
print(t)