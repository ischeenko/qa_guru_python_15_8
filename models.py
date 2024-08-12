class Product:

    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:

        return self.quantity >= quantity

    def buy(self, quantity):

        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError("Not products")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:

    products: dict[Product, int]

    def __init__(self):

        self.products = {}

    def add_product(self, product: Product, buy_count=1):

        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count


    def remove_product(self, product: Product, remove_count=None):

        if product in self.products:
            if remove_count is None or self.products[product] <= remove_count:
                del self.products[product]
            else:
                self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total = 0
        for product, count in self.products.items():
            total += product.price * count
        return total

    def buy(self):

        for product, thing in self.products.items():
            if product.quantity < thing:
                raise ValueError('Not enough products')
            else:
                product.buy(thing)
