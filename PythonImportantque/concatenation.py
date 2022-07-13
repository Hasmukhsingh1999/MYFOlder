'''' Given a single string from two given string,
a space and swap thre first two characters of each string.'''
# otp1 -> 'ebch'
# otp2 -> 'afgd'

# def swap_string(str1,str2):
#     res = str2[0] + str1[1:-1] + str2[-1]
#     res1 = str1[0] + str2[1:-1] + str1[-1]
#     return res , res1

# str1 = input("Enter the string1:")
# str2 = input("Enter the string2:")
# print(swap_string(str1,str2))

# ----------------------------------------------------------------------------------------------
'''Given a single string from a given string concatenate the second string into first string'''
# otp -> abcghdef
# def concatenate(str1,str2):
#     x = len(str1)//2
#     res = str1[0:x] + str2 + str1[x::]
#     return res

# str1 = 'abcdef'
# str2 = 'gh'
# print(concatenate(str1,str2))
# str1 = "Ault"
# str2 = "kelly"
# x = len(str1)//2
# res = str1[0:x] + str2 + str1[x::]
# print(res)
# -------------------------------------------------------------------------------------------------
# # otp -> AJrpan
# str1 = "America"
# str2 = "Japan"
# x = len(str1)//2
# y = len(str2)//2
# res = str1[0] + str2[0] + str1[x] + str2[y::]
# print(res)

# ----------------------------------------------------------------------------------------------------
# otp -> AzbycX

# str1 = 'Abc'
# str2 = 'Xyz'
# x = len(str1)//2
# y = len(str2)//2
# res = str1[0] + str2[-1] + str1[x] + str2[y] + str1[-1] + str2[0]
# print(res)

#---------------------------------------------------------------------------------------------------------

# otp -> azxcft

str1 = 'abcdef'
str2 = 'xyzst'
x = len(str1)//2
y = len(str2)//2
res = str1[0] + str2[y] +str2[0] + str1[x] + str1[-1] + str2[-1]
print(res)
