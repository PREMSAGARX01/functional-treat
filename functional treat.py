# ==========================================
# Functional Treat - Data Analyzer & Transformer
# ==========================================

dataset_summary = {}

# ------------------------------------------
# INPUT FUNCTIONS
# ------------------------------------------

def input_1d():
    """Input a 1D list from user"""
    return list(map(int, input("Enter numbers separated by spaces: ").split()))


def input_2d():
    """Input a 2D list from user"""

    rows = int(input("Enter number of rows: "))
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)

    return matrix


# ------------------------------------------
# BUILT-IN FUNCTIONS
# ------------------------------------------

def display_summary(data):
    """Display summary using built-in functions"""

    print("\n----- DATA SUMMARY -----")
    print("Total Elements :", len(data))
    print("Minimum Value  :", min(data))
    print("Maximum Value  :", max(data))
    print("Sum            :", sum(data))
    print("Average        :", round(sum(data) / len(data), 2))


# ------------------------------------------
# USER DEFINED FUNCTIONS
# ------------------------------------------

def calculate_average(data):
    """Calculate average"""
    return sum(data) / len(data)


def find_duplicates(data):
    """Find duplicate values"""

    duplicates = []

    for item in data:
        if data.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    return duplicates


def unique_values(data):
    """Return unique values"""
    return list(set(data))


# ------------------------------------------
# *ARGS
# ------------------------------------------

def show_values(*args):
    """Display values using *args"""

    print("\nValues received using *args:")

    for value in args:
        print(value)


# ------------------------------------------
# **KWARGS
# ------------------------------------------

def display_info(**kwargs):
    """Display dataset information"""

    print("\nDataset Information")

    for key, value in kwargs.items():
        print(f"{key} : {value}")


# ------------------------------------------
# RECURSION
# ------------------------------------------

def factorial(n):
    """Calculate factorial recursively"""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# ------------------------------------------
# LAMBDA FUNCTIONS
# ------------------------------------------

def filter_threshold(data):
    """Filter data using lambda"""

    threshold = int(input("Enter threshold value: "))

    filtered = list(filter(lambda x: x >= threshold, data))

    print("Filtered Data :", filtered)


def square_data(data):
    """Transform data using lambda and map"""

    result = list(map(lambda x: x * x, data))

    print("Squared Data :", result)


# ------------------------------------------
# GLOBAL VARIABLE
# ------------------------------------------

def update_global_summary(data):
    """Store summary in global variable"""

    global dataset_summary

    dataset_summary = {
        "Count": len(data),
        "Sum": sum(data),
        "Average": round(sum(data) / len(data), 2)
    }


def show_global_summary():
    """Display global summary"""

    global dataset_summary

    print("\nGlobal Dataset Summary")

    for key, value in dataset_summary.items():
        print(key, ":", value)


# ------------------------------------------
# RETURN MULTIPLE VALUES
# ------------------------------------------

def statistics(data):
    """Return multiple values"""

    minimum = min(data)
    maximum = max(data)
    average = round(sum(data) / len(data), 2)

    return minimum, maximum, average


# ------------------------------------------
# SORTING
# ------------------------------------------

def sort_1d(data):
    """Sort 1D list"""

    temp = data.copy()

    print("\n1. Ascending")
    print("2. Descending")

    choice = input("Enter choice: ")

    if choice == "1":
        temp.sort()
    else:
        temp.sort(reverse=True)

    print("Sorted Data :", temp)


def sort_2d(data):
    """Sort rows of 2D list"""

    sorted_matrix = sorted(data, key=lambda row: sum(row))

    print("\nSorted 2D List")

    for row in sorted_matrix:
        print(row)


# ------------------------------------------
# DISPLAY 2D GRID
# ------------------------------------------

def display_2d(data):
    """Display 2D list in grid format"""

    print("\n2D LIST")

    for row in data:
        for value in row:
            print(f"{value:5}", end="")
        print()


# ------------------------------------------
# DOCUMENTATION (__doc__)
# ------------------------------------------

def show_docs():
    """Display documentation strings"""

    functions = [
        input_1d,
        input_2d,
        display_summary,
        calculate_average,
        find_duplicates,
        unique_values,
        show_values,
        display_info,
        factorial,
        filter_threshold,
        square_data,
        update_global_summary,
        statistics,
        sort_1d,
        sort_2d,
        display_2d
    ]

    print("\nFUNCTION DOCUMENTATION")

    for func in functions:
        print(f"\n{func.__name__}")
        print(func.__doc__)


# ------------------------------------------
# HELPER FUNCTION
# ------------------------------------------

def flatten(data):
    """Convert 2D list into 1D list"""

    if isinstance(data[0], list):
        return [item for row in data for item in row]

    return data


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

data = []

while True:

    print("\n================================")
    print("DATA ANALYZER & TRANSFORMER")
    print("================================")
    print("1. Input 1D Data")
    print("2. Input 2D Data")
    print("3. Display Summary")
    print("4. UDF Operations")
    print("5. *args Example")
    print("6. **kwargs Example")
    print("7. Factorial (Recursion)")
    print("8. Lambda Operations")
    print("9. Global Variable")
    print("10. Return Multiple Values")
    print("11. Sorting")
    print("12. Display 2D Grid")
    print("13. Show __doc__")
    print("14. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        data = input_1d()

    elif choice == "2":
        data = input_2d()

    elif choice == "14":
        print("Thank you. Program Ended.")
        break

    else:

        if not data:
            print("Please input data first.")
            continue

        flat = flatten(data)

        if choice == "3":
            display_summary(flat)

        elif choice == "4":
            print("Average :", calculate_average(flat))
            print("Duplicates :", find_duplicates(flat))
            print("Unique Values :", unique_values(flat))

        elif choice == "5":
            show_values(10, 20, 30, 40, 50)

        elif choice == "6":
            display_info(
                Count=len(flat),
                Sum=sum(flat),
                Average=round(sum(flat) / len(flat), 2)
            )

        elif choice == "7":
            num = int(input("Enter number: "))
            print("Factorial =", factorial(num))

        elif choice == "8":
            filter_threshold(flat)
            square_data(flat)

        elif choice == "9":
            update_global_summary(flat)
            show_global_summary()

        elif choice == "10":
            mn, mx, avg = statistics(flat)

            print("Minimum :", mn)
            print("Maximum :", mx)
            print("Average :", avg)

        elif choice == "11":

            if isinstance(data[0], list):
                sort_2d(data)
            else:
                sort_1d(data)

        elif choice == "12":

            if isinstance(data[0], list):
                display_2d(data)
            else:
                print("Current data is not a 2D list.")

        elif choice == "13":
            show_docs()

        else:
            print("Invalid Choice")
