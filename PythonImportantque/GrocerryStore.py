# Write a python program Keep adding a stream of numbers input taken by the user.
# The adding stops as soon as user press q key on keyboard
sum = 0
while True:
    userinput = input("Enter the price \n")
    if userinput!='q':
        sum=sum+int(userinput)
        print(f"Order total bill so far: {sum}")
    else:
        print("Thanks for using")
        print(f"Your total bill is {sum}. Thanks for shopping with us")
        break


