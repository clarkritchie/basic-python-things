#!/usr/bin/env python3

def is_even(number):
    # Return True or False.
    return number % 2 == 0

def main():
    try:
        number = int(input("Input a number: "))
        if is_even(number):
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()