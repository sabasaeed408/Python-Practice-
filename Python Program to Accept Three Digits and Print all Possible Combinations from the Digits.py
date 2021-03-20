d1=int(input("enter the first digit"))
d2=int(input("enter the second digit"))
d3=int(input("enter the third digit"))
s=[]
s.append(d1)
s.append(d2)
s.append(d3)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(s[i],s[j],s[k])