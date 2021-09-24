from product import Product


class RestrictedProduct(Product):
    def __init__(self, age_limit=0, **kwargs):
        super().__init__(**kwargs)
        # def __init__(self, name, price, is_on_sale, age_limit):
        #     super().__init__(name, price, is_on_sale)
        self.age_limit = age_limit

    def __str__(self):
        return f"{Product.__str__(self)} [{self.age_limit}]"


def run_tests():
    rp = RestrictedProduct(name="Gun", price=125.7, is_on_sale=False, age_limit=25)
    rp.thing = 3
    beer = RestrictedProduct(name="Beer", price=5.9, is_on_sale=False, age_limit=18)
    # print(rp.thing)
    # print(beer)
    phone = Product("Phone", 123.45, True)
    print(rp == beer)
    print(rp.__eq__(beer))
    products = [rp, beer, phone]
    for product in products:
        product.put_on_sale(0.05)
        print(product)


run_tests()
