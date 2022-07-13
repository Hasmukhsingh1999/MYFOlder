# n = int(input("Enter the number : "))
# flag = False
# if n>1:
#     for i in range(2, n):
#         if n%i==0:
        
#             flag = True
#             break
# if flag:
#     print("Not a  Prime")
# else:
#     print("Number is prime")

"""Vinit is really good at maths. Recently, he came to know about a problem on prime number. Amazed by the problem he got,
he asked Sharmishtha the same problem. Sharmishtha also being good at maths solved the problem within 5 minutes. Now,
its your time to solve the problem.

"You have to generate all prime numbers between two given numbers".

Input Format
The first line of the input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of a single line containing two space separated integers m and n.

Constraints
1<=T<=60
1 <= m <= n <= 100000,
n - m <= 100000

Output Format
For every test case print all prime numbers p such that m <= p <= n, space separated. Separate the answers for each
test case by a new line.

Sample Input 0
2
1 10
3 5
Sample Output 0
2 3 5 7
3 5 """


li = []
for i in range(1,10+1):
    for j in range(2,i+1):
        if i%2!=0 and i>1 and i not in li:
            li.append(i)
print(li)
            
            


        
        
    