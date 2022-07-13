# def rotation(arr):


# arr = [5,6,9,0,2,3,4]
# print(rotation(arr))


def rotation(arr,shift):
    net_shift = abs(shift) % len(arr)-1
    for i in range(net_shift):
        if shift>0:
            popped = arr.pop(len(arr)-1)
            arr.insert(0,popped)
        if shift<0:
            popped = arr.pop(0)
            arr.append(popped)
    return arr
arr = [1,2,3,4,5,6,7]
print(rotation(arr,3))