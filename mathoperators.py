import math

# print(math.ceil(2.9))
# print(math.floor(2.9))







# If condition

# is_hot = True
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# else:
#     print("It's a cold day")
#     print("Wear warm clothes")
# print("Enjoy your day")


# # if, elif, else
#
# is_hot = True
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")



# Price of a house is $1M, if buyer has good credit they need to put down 10% otherwise they need to put down 20%. price the dwn payment


# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down Payment: ${down_payment}")
#
#

# ## If an applicant has high income AND good credit then applicant is eligible for loan
#
# has_high_income = True
# has_good_credit = True
#
# # if has_high_income and has_good_credit:
# #     print("Eligible for loan")
#
# if has_high_income or has_good_credit:
#     print("Eligible for loan")
#


# Comparison Operator


temperature = 30
if temperature < 30:
    print("It's a cold day")
else:
    print("It's a hot day")

#  if name is less than 3 characters long name must be -------------


name = "Jghffsdgsgfgfgsfdgfgsd"
if len(name) < 3:
    print("Name must be at least of three characters long")
elif len(name) > 50:
    print("Name must be maximum of 50 characters long")
else:
    print("Name looks good!")




# Project: Weight calculator


# conversion of weight from kg to lbs or lbs to kg using if else condition


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g : ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds ")






