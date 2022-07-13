''' 
Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

'''

# def binary_search(Arr,n):
#     start = 0
#     end = len(Arr)-1

#     while start <= end:
#         pivot = (start + end)//2

#         if Arr[pivot] == n :
#             return n
#         # elif Arr[pivot] !=n:
#         #     Arr.append(pivot)
        
#         elif Arr[pivot] < n :
#             end = pivot - 1

#         else:
#             start = pivot + 1

#     return -1

# Arr = list(map(int,input().split()))
# n = int(input())
# print(binary_search(Arr,n))


# --------------------------------------------------------------------------------------------


