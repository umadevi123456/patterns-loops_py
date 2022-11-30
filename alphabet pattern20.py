x=65
i=1
while i<=5:
    print(" "*(4-i),end=" ")
    j=1
    c=x
    while j-1<i:
        print(1*chr(c),end=" ")
        j+=1
        c+=1
    i+=1
    print()


