#this is a program that tells you if the number you have entered is a postive interger or a negative interager or a zero 
num = 0
num = input("please enter a number: ")
print("\n")
num = int(num)

while num != 0:
    if num > 0:
        print(num, "is a postive number")
        num = 0

    elif num < 0:
        print(num, "is a negative number")
        num = 0


