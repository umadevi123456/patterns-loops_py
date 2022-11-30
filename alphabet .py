                #    A
                #    B C
                #    D E F
                #    G H I J
                #    K L M N O
                #    P Q R S T U
                #    V W X Y Z [ \

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
