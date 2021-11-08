
def check_sublist(list_A, list_B) :
    a = False
    for i in range(len(list_A)+1) :
        for j in range(len(list_A)+1) :
            if list_A[i:j] == list_B :
                a = a or True
            else:
                a = a or False
    return a
list_A = [2, 4, 3, 5, 7]
list_B = [2, 3]
# item = int(input("nummber of list A:"))
# for i in range(1, item+1):
#     list_A.append(input())
#
# item = int(input("nummber of list B:"))
# for j in range(1, item + 1):
#     list_B.append(input())

ans = check_sublist(list_A, list_B)
print("list A :", list_A)
print("list B :", list_B)
print("Answer :", ans)




