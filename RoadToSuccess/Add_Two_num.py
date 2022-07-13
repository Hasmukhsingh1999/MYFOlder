nums =[2,7,11,15]
target = 9
res = 0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if abs(nums[0]+nums[1]==target):
            res+=1
print(res)
