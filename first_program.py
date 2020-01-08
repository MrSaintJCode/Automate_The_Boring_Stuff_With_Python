# This Program Says Hello and Ask for your Name

def hello(name,age):
    nameLen = len(name)
    print(f"\nHello {name}")
    print(f"The length of your name is {nameLen}")
    print(f"You are {age} years young!")


name = input("\nWhat is your name?\n")
age = input("\nWhat is your age? \n")
hello(name,age)