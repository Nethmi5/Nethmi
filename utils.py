def get_valid_int(prompt, min_value, max_value):
    """
    Prompt user for an integer between min_value and max_value (inclusive).
    Keeps asking until a valid integer is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def get_non_empty_string(prompt):
    """
    Prompt user for a non-empty string.
    Keeps asking until a non-empty string is entered.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")