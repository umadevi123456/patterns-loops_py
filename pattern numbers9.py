#               1  6   11   16
#               2  7   12   17
#               3  8   13   18
#               4  9   14   19
#               5  10  15   20

a=int(input("enter row number:"))                    
i=1
while i<=5:
    j=i
    while j<=a:
        print(j,end=" ")
        j+=5
    i+=1
    print()



