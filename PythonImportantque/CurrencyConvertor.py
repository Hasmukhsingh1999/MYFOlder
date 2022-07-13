with open('Currency.txt','r') as f:
    lines = f.readlines()
Currecny_dict = {}
for line in lines:
    parsed=line.split("\t")
    Currecny_dict[parsed[0]]=parsed[1]
# print(Currecny_dict)
amount  = int(input("Enter the amount\n"))
print("Enter the name of the currency you want to convert amount to : ")
print([print(item) for item in Currecny_dict.keys()])
currency = input("Enter one of these values ")
print(f" {amount} INR is eqaul to : {amount*float(Currecny_dict[currency])} {currency}")



