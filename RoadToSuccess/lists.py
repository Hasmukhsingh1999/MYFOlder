# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

# l = []
# l.insert(0,5)
# l.insert(1,10)
# l.insert(0,6)
# print(l)
# l.pop(0)
# l.append(9)
# l.append(1)
# l.sort()
# print(l)
# l.pop(3)
# print(l[::-1])

# l = [10,9,8]
# for i in l:
#     for j in range(i+1):
#         if l[j]>l[i]:
#             temp = l[i]
#             l[i]=l[j]
#             l[j]=temp
#     print(l)



# class TreeNode:
#    def __init__(self, data, left = None, right = None):
#       self.data = data
#       self.left = left
#       self.right = right
# def insert(temp,data):
#    que = []
#    que.append(temp)
#    while (len(que)):
#       temp = que[0]
#       que.pop(0)
#       if (not temp.left):
#          temp.left = TreeNode(data)
#          break
#       else:
#          que.append(temp.left)
#       if (not temp.right):
#          temp.right = TreeNode(data)
#          break
#       else:
#          que.append(temp.right)
# def make_tree(elements):
#    Tree = TreeNode(elements[0])
#    for element in elements[1:]:
#    insert(Tree, element)
#    return Tree
# class Solution(object):
#    def preorderTraversal(self, root):
#       res = []
#       st = []
#       node = root
#       while node or st:
#          while node:
#             if node.data != None:
#                res.append(node.data)
#             st.append(node)
#             node = node.left
#          temp = st[-1]
#          st.pop()
#          if temp.right:
#             node = temp.right
#    return res
# ob1 = Solution()
# head = make_tree([3,9,20,None,None,15,7])
# print(ob1.preorderTraversal(head))

# str = "agra"
# new_str = " "
# i = len(str) - 1
# while i>=0:
#    new_str+=str[i]
#    i=i-1
# print(new_str)

# x = int(input("Enter:"))
# rev = 0
# while x>0:
#    d = x%10
#    rev = rev*10 + d
#    x = x//10
# print(rev)

str = " hello"
vowel = 0
consonant = 0
l = len(str)
for i in str:
   if i == "a" or i=="e" or i=="i" or i=="o" or i=="u":
      vowel+=1
   elif i!="a" or i!="e" or i!="i" or i!="o" or i!="u":
      consonant+=1

   else:
      print(" Psu")
print(" Numbers of vowels are: " , vowel)
print("Numbers of consonats are: ",consonant)

