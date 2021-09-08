INDEX_NAME = 0
INDEX_PRICE = 1
INDEX_ON_SALE = 2
products = [["Phone", 340, False], ["PC", 1420.95, True], ["GitHub Swag", 0, False], ["Plant", 24.5, True]]

on_sale_products = [product for product in products if product[INDEX_ON_SALE]]
print(products)
print(on_sale_products)


product = ["Phone", 340, False]
# how can I put this product on sale at 10% off?
product[INDEX_PRICE] *= 0.9
product[INDEX_ON_SALE] = True
print(product)

