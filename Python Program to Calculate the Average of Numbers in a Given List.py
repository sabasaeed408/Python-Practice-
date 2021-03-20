n=int(input("enter the no of element:")) #enter the no of element in a list
a=[]   #empty list
for i in range(0,n): #loop for each element
  ele=int(input("Enter element no")) #input the no
  a.append(ele) #append the no in a list
avg=sum(a)/n #calculate the average
print(avg) #print the average
