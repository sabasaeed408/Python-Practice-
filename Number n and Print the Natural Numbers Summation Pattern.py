n=int(input("Enter the number:"))
for i in range(1,n+1):
 a=[]
 for j in range(1,i+1):
    print(j,sep="",end="")
    if(i>j):
     print("+",sep="",end="")
    a.append(j)
 print("=",sum(a))
print()