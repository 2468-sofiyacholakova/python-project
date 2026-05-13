import json
from colorama import Fore
from tabulate import tabulate


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        if self.quantity + amount >= 0:
            self.quantity += amount
            return True
        return False

    def get_total_value(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def __str__(self):
        return f"{self.name} - {self.price} lv. (Stock: {self.quantity})"


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if self.find_product(product.name):
            return False

        self.products.append(product)
        return True

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product

        return None

    def remove_product(self, name):
        product = self.find_product(name)

        if product:
            self.products.remove(product)
            return True

        return False

    def sort_by_price(self):
        return sorted(self.products, key=lambda p: p.price)

    def get_total_store_value(self):
        total = 0

        for product in self.products:
            total += product.get_total_value()

        return total

    def show_all_products(self):
        if not self.products:
            print(Fore.RED + "No products available.")
            return

        table = []

        for product in self.products:
            table.append([
                product.name,
                product.price,
                product.quantity
            ])

        print(tabulate(
            table,
            headers=["Name", "Price", "Quantity"],
            tablefmt="grid"
        ))

    def save_to_file(self, filename="products.json"):
        data = []

        for product in self.products:
            data.append(product.to_dict())

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename="products.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            for item in data:
                product = Product(
                    item["name"],
                    item["price"],
                    item["quantity"]
                )

                self.products.append(product)

        except FileNotFoundError:
            pass