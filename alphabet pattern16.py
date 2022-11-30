#       E D C B A 
#       F E D C 
#       G F E 
#       H G 
#       I

x=69
i=1
while i<6:
    j=5
    c=x
    while j>=i:
        print(chr(c),end=" ")
        j-=1
        c-=1
    i+=1
    x+=1
    print()

