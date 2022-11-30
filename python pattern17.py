#          p 
#          p y 
#          p y t 
#          p y t h 
#          p y t h o 
#          p y t h o n
        
a="python"
i=0
while i<len(a):
    j=0
    while j<=i:
        print(a[j],end=" ")
        j+=1
    i+=1
    print()

#           OR

# a=input("enter string name:")
# i=0
# while i<len(a):
#     j=0
#     while j<=i:
#         print(a[j],end=" ")
#         j+=1
#     i+=1
#     print()


a=input("enter name:")
b=" "
i=len(a)-1
while i>=0:
    b=a[i]+b
    i-=1
    print(b)







