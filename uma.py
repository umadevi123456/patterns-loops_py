# i=1
# while i<=5:
#     k=1
#     while k>=i-5:
#         print(" ",end=" ")
#         k-=1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     i+=1
#     print()

#                    M

# n=int(input("enter no:"))                    
# i=0
# while i<n:
#     k=0
#     while k<n-i-1:
#         print(" ",end="")
#         k=k+1
#     j=0
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     i=i+1
#     print( )
# i=n-1
# while i>=1:
#     k=0
#     while k<n-i:
#         print(" ",end="")
#         k=k+1
#     j=0
#     while j<i:
#         print("*",end=" ")
#         j=j+1
#     i=i-1
#     print( )

# i=1
# a=1
# while i<=3:
#     j=1
#     while j<=5:
#         print(a,end=" ")
#         j=j+1
#         a=a+1
#     i=i+1
#     print()

# i=int(input("enter the number"))
# fac=1
# while i>0:
#     fac=fac*i
#     i=i-1
# print("factorial=",fac)

# n=(input("enter number"))
# i=0
# sum=0
# while i<len(str(n)):
#     sum=sum+int(n[i])
#     i+=1
# if int(n)%sum==0:
#     print(n,"harshad number")
# else:
#     print(n,"not harshad number")

# a=int(input("number"))                         #
# n=a
# sum=0
# while a>0:
#     j=a%10
#     sum=sum+j**3
#     a=a//10
# if sum==n:
#     print(n,"armstrong number")
# else:
#     print(n,"not armstrong number")
    
b=10
a=1
i=1
while i<=5:
    j=1
    while j<=5:
        print(a,end=" ")
        a+=1
        print(b,end=" ")
        j+=1
    i+=1
    print()


