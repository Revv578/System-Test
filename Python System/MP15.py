import random
import os

def addition():
    a = random.randint(1, 101)
    b = random.randint(1, 101)
    answer = int(input(f"what is {a} plus {b}?: "))
    result = a + b
    if answer == result:
        print(f"+1")
    else:
        print(f"you got it wrong! The answer was: {result}")

def subtraction():
    a = random.randint(1, 101)
    b = random.randint(1, 101)
    answer = int(input(f"what is {a} minus {b}?: "))
    result = a - b
    if answer == result:
        print(f"+1")
    else:
        print(f"you got it wrong! The answer was: {result}")
def multiplication():
    a = random.randint(1, 101)
    b = random.randint(1, 101)
    answer = int(input(f"what is {a} multiplied by {b}?: "))
    result = a * b
    if answer == result:
        print(f"+1")
    else:
        print(f"you got it wrong! The answer was: {result}")
def division():
    a = random.randint(1, 51)
    b = random.randint(1, 51)
    if a % b != 0:
        return division()
    answer = int(input(f"what is {a} divided by {b}?: "))
    result = a / b
    if answer == result:
        print(f"+1")
    else:
        print(f"you got it wrong! The answer was: {result}")

def menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Input your choice [1-5]:"))
    return choice


def main():
    while True:
        match menu():
            case 1:
                addition()

            case 2:
                subtraction()

            case 3:
                multiplication()

            case 4:
                division()

            case 5:
                print("Thank you for playing!")
                break
main()