            #   A
            #   B B  
            #   C C C  
            #   D D D D  
            #   E E E E E

a=int(input("enter number:"))
k=ord("A")
i=1
while i<=a:
    j=1
    while j<=i:
        print(chr(k),end=" ")
        j+=1
    k+=1
    i+=1
    print()




