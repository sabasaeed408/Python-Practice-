def selectionsort(A):
    for  i in range(len(A)-1):
        minIndex=i
        for j in range(i+1,len(A)-1):
            if A[j]<A[minIndex]:
                minIndex=j
        if minIndex!=i:
            A[i],A[minIndex]=A[minIndex],A[i]
x=int(input("Number of element in a list"))
A=[]
z=0
i=0
for z in range(0,x):
    y=int(input("Insert the element "))
    A.append(y)
print(A)
s=selectionsort(A)
print(A)

