"""Product class demo - week 6 and 7"""
from product import Product

p1 = Product("Phone", 340.0, False)
p1.sku = "2134567890"
print(p1)
if p1.is_on_sale:
    print("Bargain")
else:
    print("Whatevs")
p1.put_on_sale(.9)

p2 = Product("Horse", 500, True)
print(p1)
print(p2)
result = p1.give(p2, 10000)
print(result)
print(p1)
print(p2)

# print(p2)
# p2.put_on_sale()
# print(p2)
# print(p1.default_rate, p2.default_rate)
# Product.default_rate = 0.9
# print(p1.default_rate, p2.default_rate)
#
# Product.put_on_sale(p2, 0.3)
# p2.put_on_sale(.3)
#
# str.upper("this")
# "this".upper()
# print()
# p.name = "Phone"
# p.price = 340.0
# print(p)
# things = list()
# s = str()
# things.append()

products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("GitHub Swag", 0, False),
            Product("Plant", 24.5, True)]

on_sale_products = [product for product in products if product.is_on_sale]
# print(products)
# print(on_sale_products)
