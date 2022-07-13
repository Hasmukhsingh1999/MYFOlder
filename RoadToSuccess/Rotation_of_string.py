""" Vinit and Muskan are good at string manipulation problems. One day, their biggest enemy Rewa and Mayank decided to test
their skills. They have given two strings s1 & s2 and asked to find whether s2 is a rotated version of s1. Vinit and
Muskan have no idea to solve it. They need your help.

Input Format
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows.
 Each testcase contains two lines for s1 and s2.

Constraints
1<=T<=100
1<=|s1|,|s2|<=100
The strings are lowercase.

Output Format
For each testcase, you need to print 1 if s2 is a rotated version of s1 otherwise print 0.

Sample Input 0
3
ananyachaudhary
chuadharyananya
vinitshahdeo
deovinitshah
shreyadeepanand
deepanandshreya

Sample Output 0
0
1
1"""


def rotation(s1,s2):
    new_string = " "
    l = len(s1)
    l1 = len(s2)
    if l!=l1:
        return False
    new_string = s1+s1
    if s2 in new_string:
        return 1
    else:
        return 0
T = list(map(int,input().split()))
s1 = input()
s2 = input()
print(rotation(s1,s2))





