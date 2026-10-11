"""Check divisibility of user-provided integers using common divisors."""


def divisibility_results(number: int) -> dict[int, bool]:
    """Return whether number is divisible by each common divisor."""
    divisors = (2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 15, 25, 100)
    return {divisor: number % divisor == 0 for divisor in divisors}


def check_number(number: int) -> None:
    """Print divisibility results for a single integer."""
    print(f"\nDivisibility results for {number}:")
    results = divisibility_results(number)

    for divisor, is_divisible in results.items():
        verdict = "Yes" if is_divisible else "No"
        print(f"  Divisible by {divisor:>3}: {verdict}")


def main() -> None:
    print("=== Divisibility Test Tool ===")
    print("Enter one or more integers separated by spaces or commas.")
    print("Type 'q' to quit.\n")

    while True:
        user_input = input("Enter numbers: ").strip()

        if user_input.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        if not user_input:
            print("Please enter at least one integer.\n")
            continue

        # Accept values separated by commas, spaces, or both.
        tokens = user_input.replace(",", " ").split()
        numbers = []
        invalid_tokens = []

        for token in tokens:
            try:
                numbers.append(int(token))
            except ValueError:
                invalid_tokens.append(token)

        if invalid_tokens:
            print("These entries are not valid integers: " + ", ".join(invalid_tokens))

        if not numbers:
            print("No valid integers were entered. Try again.\n")
            continue

        for number in numbers:
            check_number(number)

        print()


if __name__ == "__main__":
    main()
