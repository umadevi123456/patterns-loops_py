# 1 
# 3  2
# 6  5  4
# 10 9  8  7
# 15 14 13 12 11


a=int(input("enter row number"))
n=1
i=1
while i<=a:
    j=1
    while j<=i:
        print(n+1-j,end=" ")
        j+=1
    i+=1
    n=n+i
    print()


