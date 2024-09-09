num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


largest = num1


if num2 > largest:
    largest = num2


if num3 > largest:
    largest = num3


print("The largest number is:", largest)