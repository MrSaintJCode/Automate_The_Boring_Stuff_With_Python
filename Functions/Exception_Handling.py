import sys
def divideBy(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("[X] Error - Zero Division")
        sys.exit()


num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))
total = divideBy(num1,num2)
print(f"{num1} Divided by {num2} is: {str(total)}")