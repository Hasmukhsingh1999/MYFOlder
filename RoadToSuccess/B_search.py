'''Given an unsorted array of distinct integers and a target value, return the index if the target is found.

arr = [40, 60, 1, 200, 9, 83, 17]
---> [1,9,17,40,60,83,200] ; item = 83

output = 5 

'''

def binary_search(arr,item):
    
    start = 0
    end = len(arr)-1
    while start<=end:
        mid_value = (start + end)//2
        if arr[mid_value] == item:
            return mid_value
        elif mid_value < arr[mid_value]:
            end = mid_value -1
        else:
            start = mid_value+1

    return "%"



arr = [40, 60, 1, 200, 9, 83, 17]
item = 83
print(binary_search(arr,item))