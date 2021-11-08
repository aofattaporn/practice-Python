A = input("input :")

for i in A[::2]:
    if i.islower():
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")
# # print(list_A[::2])
#
# print(A.lower())
# print(A.upper())
# print(A.islower())
# # print(A.isupper())
# for i in B :
#     print(i)