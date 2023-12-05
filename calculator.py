#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 04, 2023
# This function,


# Calling a function named calculate
def calculate(sign, first_number, second_number):
    # setting the sign for the calculations

    if sign == "+":
        result = first_number + second_number
    elif sign == "-":
        result = first_number - second_number
    elif sign == "*":
        result = first_number * second_number
    elif sign == "/":
        result = first_number / second_number
    elif sign == "%":
        result = first_number % second_number
    else:
        result = "Invalid sign"

    return result


def main():
    # Catching any errors
    try:
        # Getting the user numbers for the operations sign to perform the operation

        user_num1 = float(input("Enter a number : "))
        user_num2 = float(input("Enter a second number : "))
        sign = input("What sign are you going to use? (+, -, *, /, %) : ")

        equation = calculate(sign, user_num1, user_num2)
        print(
            "The equation is {} {} {} = {}".format(user_num1, sign, user_num2, equation)
        )

    except ValueError as e:
        print(" {} Please enter a valid numbers.".format(e))


if __name__ == "__main__":
    main()
