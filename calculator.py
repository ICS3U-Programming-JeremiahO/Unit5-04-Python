# !/user/bin/env.python3
# Created By: Jeremiah omoike
# Date: Nov. 29, 2022
# This program asks user for 2 numbers and a symbol and calculates accordingly like a calculator


def calculate(symbol, first_number, second_number):
    if symbol == "+":
        solution = first_number + second_number
    elif symbol == "-":
        solution = first_number - second_number
    elif symbol == "*":
        solution = first_number * second_number
    elif symbol == "/":
        solution = first_number / second_number
    elif symbol == "%":
        solution = first_number % second_number
    return solution


def main():

    # asks user for the operator that they want to use
    symbol_user = input(
        "Enter the operator that you would like to use in your calculation(+, -, *, /, %, ): "
    )

    if (
        symbol_user == "+"
        or symbol_user == "-"
        or symbol_user == "*"
        or symbol_user == "/"
        or symbol_user == "%"
    ):
        print()
        # asks user for the first number that they want to use in their operation
        first_number_string = input("Enter your first number here: ")
        try:
            first_number_float = float(first_number_string)

            print()
            # asks user for the second number that they want to use in their equation
            second_number_string = input("Enter your second number here: ")
            try:
                second_number_float = float(second_number_string)

                # assigns variable to function call that gives return value
                solution_user = calculate(
                    symbol_user, first_number_float, second_number_float
                )
                print()
                print(
                    " The result of {} {} {} = {}".format(
                        first_number_float,
                        symbol_user,
                        second_number_float,
                        solution_user,
                    )
                )
            # catches any invalid input
            except Exception:
                print()
                print("{} is not a valid number. ".format(second_number_string))
        # catches any invalid input
        except Exception:
            print()
            print("{} is not a valid number.".format(first_number_string))
    # catches any invalid input
    else:
        print()
        print("{} is not a valid operator".format(symbol_user))


if __name__ == "__main__":
    main()
