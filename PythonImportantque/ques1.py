#Add item 70 after 60 in the following List
# li = [10, 20, [30, 40, [50, 60], 80], 90, 100]
# li[2][2].append(70)
# print(li)


list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    x = list1.index(20)
    list1[x]=200
print(list1)
