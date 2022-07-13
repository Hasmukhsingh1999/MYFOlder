def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] =temp
   

    return arr

arr = list(map(int,input().split()))
print(bubble_sort(arr))



def bubble_sorting(list_a):
    indexing = len(list_a)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(indexing):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i] , list_a[i+1] = list_a[i+1] , list_a[i]
    return list_a

list_a = list(map(int,input().split()))
print(bubble_sorting(list_a))
