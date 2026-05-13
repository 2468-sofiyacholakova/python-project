from colorama import Fore, init
from models import Product, Store

init()


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print(Fore.RED + "Invalid input. Please enter an integer.")


def menu():
    print(Fore.CYAN + "\n--- TECH STORE MENU ---")
    print("1. Add product")
    print("2. Show all products")
    print("3. Find product")
    print("4. Update quantity")
    print("5. Remove product")
    print("6. Sort by price")
    print("7. Total store value")
    print("0. Exit")


def main():
    store = Store()

    store.load_from_file()

    while True:
        menu()

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Product name: ")

            price = get_float("Price: ")

            while price <= 0:
                print(Fore.RED + "Price must be positive.")
                price = get_float("Price: ")

            quantity = get_int("Quantity: ")

            while quantity < 0:
                print(Fore.RED + "Quantity cannot be negative.")
                quantity = get_int("Quantity: ")

            product = Product(name, price, quantity)

            if store.add_product(product):
                print(Fore.GREEN + "Product added.")

            else:
                print(Fore.RED + "Product already exists.")

        elif choice == "2":
            store.show_all_products()

        elif choice == "3":
            name = input("Enter product name: ")

            product = store.find_product(name)

            if product:
                print(Fore.GREEN + str(product))

            else:
                print(Fore.RED + "Product not found.")

        elif choice == "4":
            name = input("Product name: ")

            amount = get_int("Quantity to add/remove: ")

            product = store.find_product(name)

            if product:
                if product.update_quantity(amount):
                    print(Fore.GREEN + "Quantity updated.")

                else:
                    print(Fore.RED + "Not enough stock.")

            else:
                print(Fore.RED + "Product not found.")

        elif choice == "5":
            name = input("Product name: ")

            if store.remove_product(name):
                print(Fore.GREEN + "Product removed.")

            else:
                print(Fore.RED + "Product not found.")


        elif choice == "6":

            store.products = store.sort_by_price()

            store.show_all_products()

        elif choice == "7":
            total = store.get_total_store_value()

            print(Fore.YELLOW + f"Total store value: {total} lv.")

        elif choice == "0":
            store.save_to_file()

            print(Fore.CYAN + "Products saved.")
            print(Fore.CYAN + "Exiting program.")

            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main()