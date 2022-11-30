#                  1 1 1 1 1
#                  2 2 2 2 
#                  3 3 3
#                  4 4
#                  5


a=int(input("enter number:"))
i=0
while i<a:
    j=a
    while j>i:
        print(i+1,end=" ")
        j-=1
    i+=1
    print()
