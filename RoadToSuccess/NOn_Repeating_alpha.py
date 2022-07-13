'''Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return '$'.

Example 1:

Input:
S = hello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.
Example 2:

Input:
S = zxvczbtxyzvy
Output: c
Explanation: In the given string, 'c' is
the character which is non-repeating. '''

# def non_repeating(s):
#     dic = {}
#     for i in range(len(s)):
#         if s[i] not in dic:
#             dic[s[i]]=1
#         else:
#             dic[s[i]]+=1
            
#     for i in range(len(s)):
#         if dic[s[i]]==1:
#             return s[i]
#         return '$'



# s = input("Enter the string : ")
# print(non_repeating(s))
    
# s = "zxvczbtxyzvy"
# dic = {}
# stack = []
# for i in s:
#     if i  in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
#         stack.append(i)
        
# for i in stack:
#     if dic[s] == 1:
#         print(i)
# #     print("$")
    
# for key,value in dic.items():
#     print(key,value)
def firstNonRepeatingChar(str1):
   char_order = []
   counts = {}
   for c in str1:
      if c in counts:
         counts[c] += 1
      else:
         counts[c] = 1
         char_order.append(c)
   for c in char_order:
      if counts[c] == 1:
        return c
   return None


print(firstNonRepeatingChar('hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs'))