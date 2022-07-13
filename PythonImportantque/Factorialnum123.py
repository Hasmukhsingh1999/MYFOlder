# PART-I Calculate the factorial of a given number
# PART-II Find the  number of tailing zeroes in that factorial
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
def factorialTrailingZeros(num):
    count = 0
    #100! = 100//5 + 100//5*5
    i=5
    while num//i!=0:
        count += int(num/i)
        i=i*5
    return count

if __name__ == '__main__':
    num = int(input("Enter any num: "))
    print(f"The factorail of {num} is : {factorial(num)}")
    print(factorialTrailingZeros(num))


# def factorial(n):
#     num=1
#     while n!=0:
#         num = num*n
#         n=n-1
#     return num
# f = factorial(4)
# print(f)
