"""Simple command-line calculator.

Supports addition, subtraction, multiplication, division, and modulus.
Run with: python calculator.py
"""


def calculate(first: float, operator: str, second: float) -> float:
    """Perform a calculation and return the result."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    if operator == "%":
        if second == 0:
            raise ZeroDivisionError("Cannot calculate modulus by zero.")
        return first % second

    raise ValueError("Unsupported operator. Use +, -, *, /, or %.")


def main() -> None:
    print("=== Python Calculator ===")
    print("Operators: +  -  *  /  %")
    print("Type 'q' at the operator prompt to quit.\n")

    while True:
        try:
            first_text = input("Enter the first number: ").strip()
            first = float(first_text)

            operator = input("Enter an operator (+, -, *, /, %): ").strip()
            if operator.lower() == "q":
                print("Goodbye!")
                break

            second = float(input("Enter the second number: ").strip())
            result = calculate(first, operator, second)
            print(f"Result: {result:g}\n")

        except ValueError as error:
            print(f"Input error: {error}\n")
        except ZeroDivisionError as error:
            print(f"Math error: {error}\n")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
