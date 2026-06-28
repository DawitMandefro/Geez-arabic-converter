# converter.py

from arabic_to_geez import convert_to_geez
from geez_to_arabic import convert_to_arabic


def display_menu():
    print("\n========== Geez-Arabic Number Converter ==========")
    print("1. Arabic to Geez")
    print("2. Geez to Arabic")
    print("3. Exit")


def main():
    while True:
        display_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                number = int(input("Enter an Arabic number: "))
                result = convert_to_geez(number)
                print(f"\nGeez Number: {result}")

            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        elif choice == "2":
            geez = input("Enter a Geez number: ")
            result = convert_to_arabic(geez)
            print(f"\nArabic Number: {result}")

        elif choice == "3":
            print("Thank you for using the Geez-Arabic Number Converter.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        while True:
            again = input("\nDo you want to perform another conversion? (y/n): ").lower()

            if again == "y":
                break

            elif again == "n":
                print("Thank you for using the Geez-Arabic Number Converter.")
                return

            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
