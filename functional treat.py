"""
Data Analyzer and Transformer Program

This program demonstrates:
- built-in functions
- user-defined functions
- *args and **kwargs
- __doc__
- recursion
- lambda
- global keyword
- returning multiple values
- 1D and 2D list handling
- sorting
"""

data_1d = []
data_2d = []
summary = {"total": 0, "mean": 0}


def input_1d():
    """Take 1D list input from the user."""
    global data_1d

    print("\n--- Input 1D Data ---")
    text = input("Enter numbers separated by spaces: ").strip()

    if text == "":
        data_1d = []
        print("No data entered.")
        return

    try:
        data_1d = [int(x) for x in text.split()]
        print("1D data stored successfully.")
    except ValueError:
        print("Only numbers are allowed.")
        data_1d = []


def input_2d():
    """Take 2D list input from the user."""
    global data_2d

    print("\n--- Input 2D Data ---")

    try:
        rows = int(input("How many rows? "))
        cols = int(input("How many columns in each row? "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    temp = []
    for i in range(rows):
        while True:
            try:
                row = input(f"Enter row {i + 1} values separated by spaces: ").strip()
                values = [int(x) for x in row.split()]

                if len(values) != cols:
                    print(f"Please enter exactly {cols} values.")
                    continue

                temp.append(values)
                break
            except ValueError:
                print("Only numbers are allowed.")

    data_2d = temp
    print("2D data stored successfully.")


def update_summary():
    """Update global summary values using the current 1D data."""
    global summary

    if len(data_1d) == 0:
        summary = {"total": 0, "mean": 0}
    else:
        summary["total"] = sum(data_1d)
        summary["mean"] = sum(data_1d) / len(data_1d)


def show_summary():
    """Display basic statistics using built-in functions."""
    print("\n--- Data Summary ---")

    if len(data_1d) == 0:
        print("No 1D data available.")
        return

    print("Total elements:", len(data_1d))
    print("Minimum value:", min(data_1d))
    print("Maximum value:", max(data_1d))
    print("Sum of values:", sum(data_1d))
    print("Average value:", round(sum(data_1d) / len(data_1d), 2))

    update_summary()


def get_statistics():
    """Return multiple values: minimum, maximum, sum and average."""
    if len(data_1d) == 0:
        return None, None, None, None

    minimum = min(data_1d)
    maximum = max(data_1d)
    total = sum(data_1d)
    average = total / len(data_1d)

    return minimum, maximum, total, average


def display_statistics():
    """Show the values returned by get_statistics()."""
    print("\n--- Dataset Statistics ---")

    minimum, maximum, total, average = get_statistics()

    if minimum is None:
        print("No 1D data available.")
        return

    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Sum of values:", total)
    print("Average value:", round(average, 2))


def factorial(n):
    """Calculate factorial using recursion."""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def show_factorial():
    """Ask the user for a number and display factorial."""
    print("\n--- Factorial (Recursion) ---")

    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    result = factorial(n)

    if result is None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {n} is: {result}")


def filter_data():
    """Filter 1D data using lambda and filter()."""
    print("\n--- Filter Data Using Lambda ---")

    if len(data_1d) == 0:
        print("No 1D data available.")
        return

    try:
        threshold = int(input("Enter threshold value: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    condition = lambda x: x >= threshold
    result = list(filter(condition, data_1d))

    print(f"Filtered values (>= {threshold}):")
    if len(result) == 0:
        print("No matching values.")
    else:
        print(", ".join(map(str, result)))


def sort_data():
    """Sort 1D data and 2D rows."""
    print("\n--- Sort Data ---")

    if len(data_1d) == 0 and len(data_2d) == 0:
        print("No data available.")
        return

    print("1. Sort 1D data")
    print("2. Sort 2D rows")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("1. Ascending")
        print("2. Descending")
        order = input("Enter order: ")

        if len(data_1d) == 0:
            print("No 1D data available.")
            return

        if order == "1":
            data_1d.sort()
            print("Sorted 1D data:", ", ".join(map(str, data_1d)))
        elif order == "2":
            data_1d.sort(reverse=True)
            print("Sorted 1D data:", ", ".join(map(str, data_1d)))
        else:
            print("Invalid order.")

    elif choice == "2":
        if len(data_2d) == 0:
            print("No 2D data available.")
            return

        print("1. Sort rows by first value")
        print("2. Sort rows by row sum")

        option = input("Enter your choice: ")

        if option == "1":
            sorted_rows = sorted(data_2d, key=lambda row: row[0])
            print("\nSorted 2D data:")
            display_2d_list(sorted_rows)

        elif option == "2":
            sorted_rows = sorted(data_2d, key=sum)
            print("\nSorted 2D data:")
            display_2d_list(sorted_rows)

        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")


def display_2d_list(arr):
    """Display a 2D list in grid form."""
    print("\n--- 2D Data ---")

    if len(arr) == 0:
        print("No 2D data available.")
        return

    for row in arr:
        print(" | ".join(map(str, row)))


def show_args(*args):
    """Display values passed using *args."""
    print("\n--- *args Demo ---")
    if len(args) == 0:
        print("No values passed.")
        return

    print("Values passed:")
    for item in args:
        print(item)


def show_kwargs(**kwargs):
    """Display key-value pairs passed using **kwargs."""
    print("\n--- **kwargs Demo ---")
    if len(kwargs) == 0:
        print("No key-value pairs passed.")
        return

    for key, value in kwargs.items():
        print(f"{key}: {value}")


def show_docstrings():
    """Print the docstring of each function."""
    print("\n--- Function Descriptions (__doc__) ---")
    functions = [
        input_1d, input_2d, update_summary, show_summary, get_statistics,
        display_statistics, factorial, show_factorial, filter_data,
        sort_data, display_2d_list, show_args, show_kwargs
    ]

    for func in functions:
        print(f"\n{func.__name__}:")
        print(func.__doc__)


def show_menu():
    """Display the main menu."""
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input 1D Data")
    print("2. Input 2D Data")
    print("3. Display Data Summary")
    print("4. Calculate Factorial")
    print("5. Filter Data by Threshold")
    print("6. Sort Data")
    print("7. Display Dataset Statistics")
    print("8. Display 2D Data")
    print("9. *args Demo")
    print("10. **kwargs Demo")
    print("11. Show Function Descriptions")
    print("12. Exit Program")


while True:
    show_menu()
    choice = input("Please enter your choice: ")

    if choice == "1":
        input_1d()

    elif choice == "2":
        input_2d()

    elif choice == "3":
        show_summary()

    elif choice == "4":
        show_factorial()

    elif choice == "5":
        filter_data()

    elif choice == "6":
        sort_data()

    elif choice == "7":
        display_statistics()

    elif choice == "8":
        display_2d_list(data_2d)

    elif choice == "9":
        show_args(10, 20, 30, "hello", True)

    elif choice == "10":
        show_kwargs(name="Alice", age=20, grade="B+")

    elif choice == "11":
        show_docstrings()

    elif choice == "12":
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
