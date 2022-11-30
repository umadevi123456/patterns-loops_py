# 2
# 4  2
# 6  4  2
# 8  6  4  2
# 10 8  6  4  2

a=int(input("enter row numbers:"))
i=1
while i<=a:
    j=i
    while j>=1:
        print(j+1,end="  ")
        j=j-2
    i+=2
    print()
    



