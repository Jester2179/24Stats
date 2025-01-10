import statistics
from typing import List

def display_menu():
    print("\n=== List Operations Menu ===")
    print("1. Add item to list")
    print("2. Remove item by value")
    print("3. Remove item by position")
    print("4. Display list")
    print("5. Compute mean")
    print("6. Compute median")
    print("7. Compute midpoint")
    print("8. Compute mode(s)")
    print("9. Compute standard deviation")
    print("10. Exit")

def add_item(numbers: List[float]):
    try:
        num = float(input("Enter a number to add: "))
        numbers.append(num)
        print(f"{num} has been added to the list.")
    except ValueError:
        print("Please enter a valid number.")

def remove_by_value(numbers: List[float]):
    if not numbers:
        print("List is empty!")
        return
    try:
        value = float(input("Enter the value to remove: "))
        if value in numbers:
            numbers.remove(value)
            print(f"{value} has been removed.")
        else:
            print("Value not found in list.")
    except ValueError:
        print("Please enter a valid number.")

def remove_by_position(numbers: List[float]):
    if not numbers:
        print("List is empty!")
        return
    try:
        pos = int(input(f"Enter position (0-{len(numbers)-1}): "))
        if 0 <= pos < len(numbers):
            removed = numbers.pop(pos)
            print(f"Number {removed} at position {pos} removed.")
        else:
            print("Invalid position!")
    except ValueError:
        print("Please enter a valid position number.")

def compute_midpoint(numbers: List[float]):
    if not numbers:
        print("List is empty!")
        return
    min_val = min(numbers)
    max_val = max(numbers)
    midpoint = (min_val + max_val) / 2
    print(f"Midpoint: {midpoint}")

def main():
    numbers = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            add_item(numbers)
        elif choice == '2':
            remove_by_value(numbers)
        elif choice == '3':
            remove_by_position(numbers)
        elif choice == '4':
            print("Current list:", numbers)
        elif choice == '5':
            if numbers:
                print(f"Mean: {statistics.mean(numbers)}")
            else:
                print("List is empty!")
        elif choice == '6':
            if numbers:
                print(f"Median: {statistics.median(numbers)}")
            else:
                print("List is empty!")
        elif choice == '7':
            compute_midpoint(numbers)
        elif choice == '8':
            if numbers:
                print(f"Mode(s): {statistics.multimode(numbers)}")
            else:
                print("List is empty!")
        elif choice == '9':
            if len(numbers) >= 2:
                print(f"Standard Deviation: {statistics.stdev(numbers)}")
            else:
                print("Need at least 2 numbers for standard deviation!")
        elif choice == '10':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()