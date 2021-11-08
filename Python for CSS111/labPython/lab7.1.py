# list_A = [2, 4, 3, 5, 7]
# list_B =[]
# for i in range(len(list_A)+1) :
#     for j in range(len(list_A)+1) :
#         if list_A[i:j] == list_B:
#             print(True)
item = [1, 2, 3]
item2 = [3, 4, 5]
a = False
for i in item :
    for j in item2 :
        if i == j :
            a = a or True
            break
        else:
            a = a or False
print(a)