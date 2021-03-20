n=int(input("Enter the number"))
t=0
count=0
for i in range(0,n):
   if(n%10>0):
      count=count+1
      n= n//10
print(count)


