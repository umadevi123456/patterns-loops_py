# 1
# *
# 2
# **
# 3
# ***
# 4
# ****
# 5
# *****

i=1
while i<=5:
    j=i
    while j<=i:
        print(j)
        print(j*"*")
        j+=1
    i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=1
#     print()
#     k=1
#     while k<=i:
#         print("*",end=" ")
#         k=k+1
#     i+=1
#     print()

