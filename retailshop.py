class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def apply_discount(self):
        return 0

    def get_category(self):
        return "Product"


class GroceryProduct(Product):
    def apply_discount(self):
        return self.get_price() * self.get_quantity() * 0.05

    def get_category(self):
        return "Grocery"


class ElectronicsProduct(Product):
    def apply_discount(self):
        return self.get_price() * self.get_quantity() * 0.10

    def get_category(self):
        return "Electronics"

class ClothingProduct(Product):
    def apply_discount(self):
        return self.get_price() * self.get_quantity() * 0.15

    def get_category(self):
        return "Clothing"

class Loyalty:
    def __init__(self, tier):
        self.tier = tier

    def get_discount(self):
        if self.tier == "Silver":
            return 0.05
        elif self.tier == "Gold":
            return 0.10
        elif self.tier == "Regular":
            return 0

class BillingEngine:
    def __init__(self, cart, loyalty):
        self.cart = cart
        self.loyalty = loyalty

    def generate_bill(self):
        subtotal = 0
        category_discount = 0

        print("\n=============RETAIL STORE BILL=============")
        print(f"{'Product':<15}{'Qty':<5}{'Price':<10}{'Discount':<12}{'Total':<10}")
        print("---------------------------------------------")
        for item in self.cart:
            original = item.get_price() * item.get_quantity()
            discount = item.apply_discount()
            final_price = original - discount

            subtotal += original
            category_discount += discount

            print(f"{item.get_name():<15}{item.get_quantity():<5}"
                  f"{item.get_price():<10.2f}{discount:<12.2f}"
                  f"{final_price:<10.2f}")

        amount_after_discount = subtotal - category_discount

        loyalty_discount = amount_after_discount * self.loyalty.get_discount()
        grand_total = amount_after_discount - loyalty_discount

        print("---------------------------------------------")
        print(f"Subtotal:  Rs. {subtotal:.2f}")
        print(f"Category Discounts: Rs. {category_discount:.2f}")
        print(f"Amount After Discounts: Rs. {amount_after_discount:.2f}")
        print(f"Loyalty Tier: {self.loyalty.tier}")
        print(f"Loyalty Discount: Rs. {loyalty_discount:.2f}")
        print(f"Grand Total: Rs. {grand_total:.2f}")


cart = []

a = input("Enter the Number of products in the cart:")
for i in range(int(a)):
    product_name = input("Enter the product name:")
    product_price = float(input("Enter the product price:"))
    product_quantity = int(input("Enter the product quantity:"))
    product_category = input("Enter the product category (Grocery/Electronics/Clothing):")
    loyalty_tier = input("Enter the loyalty tier (Silver/Gold/Regular):")

    if product_category.lower() == "grocery":
        product = GroceryProduct(product_name, product_price, product_quantity)
    elif product_category.lower() == "electronics":
        product = ElectronicsProduct(product_name, product_price, product_quantity)
    elif product_category.lower() == "clothing":
        product = ClothingProduct(product_name, product_price, product_quantity)
    else:
        print("Invalid category. Product not added.")
        continue

    if loyalty_tier.lower() == "silver" or loyalty_tier.lower() == "gold" or loyalty_tier.lower() == "regular":
        loyalty = Loyalty(loyalty_tier)
    else:
        print("Invalid loyalty tier.")
        continue

    cart.append(product)

billing = BillingEngine(cart, loyalty)
billing.generate_bill()
