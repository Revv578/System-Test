import os
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)

def biggest(arr):
    if len(arr) == 1:
        return arr[0]
    largest = biggest(arr[1:])
    if arr[0] > largest: 
        return arr[0]
    else:
        return largest

def digit_count(n):
    if n < 10:
        return 1
    else:
        return 1 + digit_count(n // 10)

def sum_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sum_digits(n // 10)# example: 12345 -> 5 + sum_digits(1234) -> 5 + 4 + sum_digits(123) -> 5 + 4 + 3 + sum_digits(12) -> 5 + 4 + 3 + 2 + sum_digits(1) -> 5 + 4 + 3 + 2 + 1

def is_sorted(arr):
    if len(arr) == 1:
        return True
    else:
        if arr[0] < arr[1]:
            return is_sorted(arr[1:])
        else:
            return False
        
def int_palindrome(n, reversed=0, default = None):
    if default is None:
        default = n
    if n == 0:
        return reversed == default
    return int_palindrome(n//10, reversed * 10 + n % 10, default)

def arr_palindrome(arr):
    if len(arr) <= 1:
        return True
    else:
        if arr[0] == arr[-1]:
            return arr_palindrome(arr[1:-1])
        else:
            return False
        
def prime(n, i = 2):
    if n < 2:
        return False
    if n == i:
        return True
    elif n % i == 0: 
        return False
    return prime(n, i + 1)

def gcd(b, s):
    if b%s == 0:
        return s
    return gcd(s, b % s)

def print_to_n(n,walk):
    if n == 1:
        return 
    if n == walk:
        print(walk)
        return 
    else:
        print(walk)
        print_to_n(n, walk+1)

def sum_arr(arr, i = 0):
    if i == len(arr):
        return 0
    return arr[i] + sum_arr(arr, i + 1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_print():
    print("FUNCTIONS")
    print("1. factorial")
    print("2. biggest")
    print("3. digit_count")
    print("4. Sum of Digits")
    print("5. isSorted")
    print("6. isPalindrome (int)")
    print("7. isPalindrome (arr)")
    print("8. isPrime")
    print("9. GCD")
    print("10. 1 to n")
    print("11. Sum of arr")
    print("0. Exit")
    return int(input("enter choice 1-11: "))

def test():
    print(factorial(5))
    print(biggest([1, 2, 3, 4, 5])) 
    print(digit_count(12345))  
    print(sum_digits(12345))
    print(is_sorted([1, 2, 3, 4, 5]))
    print(int_palindrome(12321))    
    print(arr_palindrome([1, 2, 3, 2, 1]))
    print(prime(7))
    print(gcd(48, 18))
    print_to_n(5, 1)
    print(sum_arr([1, 2, 3, 4, 5]))
    print("Press enter to input...")
    os.system("pause")


def main():
    while True:
        clear_screen()
        match menu_print():
            case 1:
                clear_screen()
                print(factorial(int(input("enter n: "))))
                input("press enter to continue...")
            case 2:
                clear_screen()
                print(biggest(list(map(int, input("enter elements: ").split()))))
                input("press enter to continue...")
            case 3:
                clear_screen()
                print(digit_count(int(input("enter n: "))))
                input("press enter to continue...")
            case 4:
                clear_screen()
                print(sum_digits(int(input("enter n: "))))
                input("press enter to continue...")
            case 5:
                clear_screen()
                print(is_sorted(list(map(int, input("enter elements: ").split()))))
                input("press enter to continue...")
            case 6:
                clear_screen()
                print(int_palindrome(int(input("enter n: "))))
                input("press enter to continue...")
            case 7:
                clear_screen()
                print(arr_palindrome(list(map(int, input("enter elements: ").split()))))
                input("press enter to continue...")
            case 8:
                clear_screen()
                print(prime(int(input("enter n: "))))
                input("press enter to continue...")
            case 9:
                clear_screen()
                print(gcd(int(input("enter n: ")), int(input("enter n: "))))
                input("press enter to continue...")
            case 10:
                clear_screen()
                print_to_n(int(input("enter n: ")), 1)
                input("press enter to continue...")
            case 11:
                clear_screen()
                print(sum_arr(list(map(int, input("enter elements: ").split()))))
                input("press enter to continue...")
            case 0:
                clear_screen()
                break

if __name__ == '__main__':
    test()
    main()