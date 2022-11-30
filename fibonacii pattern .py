n=int(input("enter number:"))
n1=0
n2=1
r=n1+n2
i=0
while i<n:
    j=0
    while j<=i:
        print(str(r)+" ",end="")
        r=n1+n2
        n1=n2
        n2=r
        j+=1
    i+=1
    print()
    
