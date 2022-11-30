# num=int(input("enter any number:"))
# i=1
# while i<=num:
#     print(" "*(num-i)+"* "*i)
#     i+=1

    #      *
    #     * *
    #    * * *
    #   * * * *
    #  * * * * *

a=int(input("enter row number:"))                       
i=1
while i<=a:
    k=1
    while k<=a-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print()


