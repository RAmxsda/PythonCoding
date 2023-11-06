def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)

    operation_symbol = input("\nPick an operation from the line above: ")

    isCalculating = False
    while not isCalculating:
        num2 = float(input("Enter the next number: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_calculation = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n"
        )
        if next_calculation == "y":
            num1 = answer

        elif next_calculation == "n":
            isCalculating = True
            calculator()
        else:
            exit()


calculator()
