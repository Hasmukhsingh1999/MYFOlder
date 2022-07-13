# import string
# import random
#
# if __name__ == '__main__':
#     set_char1 = string.ascii_lowercase
#     # print(set_char1)
#     set_char2 = string.ascii_uppercase
#     # print(set_char2)
#     set_char3 = string.digits
#     # print(set_char3)
#     set_char4 = string.punctuation
#     # print(set_char4)
#     passwlen = int(input("Enter the password length\n"))
#     s = []
#     s.extend(list(set_char1))
#     s.extend(list(set_char2))
#     s.extend(list(set_char3))
#     s.extend(list(set_char4))
#     # print(s)
#     random.shuffle(s)
#     # print(s)
#     print("Your password is : ")
#     print("".join(s[0:passwlen]))

Secure = (('S','$') , ('And','&') , ('a','@'))


def securePassword(password):
    for a,b in Secure:
        password=password.replace(a,b)

    return password


if __name__ == '__main__':
    password = input("Enter your password")
    password = securePassword(password)
    print(f"Your secure password is {password}")


