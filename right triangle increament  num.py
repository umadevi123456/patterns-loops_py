    #   1 1 1 1 1 
    #   2 2 2 2
    #   3 3 3
    #   4 4
    #   5

# i=1
# j=5
# while i<=5:
#     print(str(i)*j,end=" ")
#     i=i+1
#     j=j-1
#     print()

a=int(input("enter row numbber:"))
i=1
while i<=a:
    j=i
    while j<=a:
        print(i,end=" ")
        j+=1
    i+=1
    print()
