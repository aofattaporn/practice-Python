list_x = ["a", "bc", 123]
def list_compare(item, item2):
    a = False
    for i in item :
        for j in item2 :
            if i == j :
                a = a or True
                break
            else:
                a = a or False
    return a
list_A = [1, 2, 3]
list_B = ["a", "2", 3]
# item = int(input("nummber of list A:"))
# for i in range(1, item+1):
#     list_A.append(input())

ans = (input("Do you want to make a list B (yes/no):"))

if ans == "yes" :
    # item = int(input("nummber of list B:"))
    # for j in range(1, item + 1):
    #     list_B.append(input())
    print(list_compare(list_A, list_B))
else:
    print(list_compare(list_A, list_x))