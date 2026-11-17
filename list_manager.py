# list_manager.py

numbers = []

while True:
    print("\n--- List Manager ---")
    print("a. Add a number")
    print("b. Remove a number")
    print("c. Display list")
    print("d. Quit")

    choice = input("Choose an option: ").lower()

    if choice == "a":
        try:
            num = int(input("Enter an integer: "))
            numbers.append(num)
            print(f"{num} added to the list.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    elif choice == "b":
        try:
            index = int(input("Enter the index to remove: "))
            removed = numbers.pop(index)
            print(f"Removed {removed} from the list.")
        except ValueError:
            print("Error: Please enter a valid integer index.")
        except IndexError:
            print("Error: Invalid index. Please try again.")

    elif choice == "c":
        print("Current List:", numbers)

    elif choice == "d":
        print("Exiting program...")
        break

    else:
        print("Error: Invalid menu option.")
