# def selection_sort(list_a):
#     indexing_length = range(0, len(list_a)-1)

#     for i in indexing_length:
#         min_value = i

#         for j in range(i+1, len(list_a)):
#             if list_a[j] <  list_a[min_value]: #"angled brackets not allowed in youtube description"
#                 min_value = j


#         if min_value != i:
#             list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

#     return list_a

# print(selection_sort([7,8,9,8,7,6,5,6,7,8,9,0]))



# def selection_sort(arr):
#     for i in range(0,len(arr)-1):
#         min_pos = i

#         for j in range(i+1 , len(arr)):
#             if arr[j]<arr[min_pos]:
#                 min_pos = j

#         if min_pos != i:
#             temp = arr[i]
#             arr[i] = arr[min_pos]
#             arr[min_pos] = temp
#     return arr
# print(selection_sort([7,8,9,8,7,6,5,6,7,8,9,0]))

def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_os = i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_os]:
                min_os = j

        if i!= min_os:
            arr[i], arr[min_os] = arr[min_os] , arr[i]
    return arr

arr = [78,12,15,8,61,53,23,27]
print(selection_sort(arr))   