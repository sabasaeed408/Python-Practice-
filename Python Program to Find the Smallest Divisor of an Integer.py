n=int(input("Enter the element to find the smallest divisor"))
for i in range(2,n):
    if(n%i==0):
        print(i)
        break