r=5
c=5
i=1
while i<=r:
    j=1
    while j<=c:
        if j==1 or   j==5 or i==1 or i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()




