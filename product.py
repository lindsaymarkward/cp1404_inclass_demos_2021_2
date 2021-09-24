"""Product class file."""


class Product:
    """Product class to store data for a saleable product."""

    default_rate = 0.2  # class variable (shared)

    def __init__(self, name="", price=0.0, is_on_sale=False):
        """Initialise a Product class."""
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale
        self.sku = ""

    def __str__(self):
        """Represent a Product as a string."""
        on_sale_message = " (on sale!)" if self.is_on_sale else ""
        return f"{self.name} (SKU: {self.sku}) costs ${self.price:.2f}{on_sale_message} ({self.default_rate}%)"

    def __repr__(self):
        """..."""
        return str(self)

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.price == other.price

    def put_on_sale(self, discount_rate=default_rate):
        """Method docstring."""
        self.price *= (1 - discount_rate)
        self.is_on_sale = True

    @staticmethod
    def cheer():
        """..."""
        print("YAY!")
        # TODO: make this useful

    def give(self, other, amount):
        """Give a taco - TODO remove"""
        if self.price - amount < 0:
            return False
        self.price -= amount
        other.price += amount
        return True


if __name__ == '__main__':
    print("Hello!")
