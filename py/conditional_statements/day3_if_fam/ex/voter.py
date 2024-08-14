#2. If the user is eligible
'''
voter = int(input('Enter the age: '))

if voter>=5 and voter<80:
    print("Please enter a valid age")
    if voter>=18:
        print("Eligible")
else:
    print("Ineligible")
'''


# 3. find the greatest of 3 numbers
'''
var1, var2, var3 = int(input('Enter the 1st 2nd and 3rd number: '))
if var1 > var2 and var1 > var3:
    print(var1,"is the greatest number")
elif var2 > var3 and var2 > var1:
    print(var2,"is the greatest number")
elif var3 > var2 and var3 > var1:
    print(var3,"is the greatest number")
else:
    print("Input values are equal")

'''

# 4. take the divisor and divident as input and find if it is divisible
'''
val1 = int(input('Enter the first value: '))
val2 = int(input('Enter the second value: '))
if val2 > val1:
    if val2 % val1 == 0:
        print(val2,"is divisible by" ,val1)
    else:
        print(val2,"is not divisible by" ,val1)
else:
    print("enter valid input")
'''

alpha = input('Enter the alpha: ')
#1
if alpha in 'aeiou':
    print(alpha, "is a vowel")
else:
    print(alpha, "is not a vowel")
#2
val = ['a', 'e', 'i', 'o', 'u']
if alpha in val:
    print(alpha, "is a vowel")
else:
    print(alpha, "is not a vowel")