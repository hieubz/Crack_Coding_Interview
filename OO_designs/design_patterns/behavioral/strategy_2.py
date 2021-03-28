
class Item:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self._discount_strategy = discount_strategy

    def display_price(self):
        if self._discount_strategy:
            discount = self._discount_strategy(self)
        else:
            discount = 0
        print(f"the price is {self.price - discount}")


def on_sale_discount(item: Item):
    return item.price * 0.25


def normal_discount(item: Item):
    return item.price * 0.2


if __name__ == '__main__':
    item = Item(100, discount_strategy=on_sale_discount)
    item_2 = Item(100, discount_strategy=normal_discount)
    item.display_price()
    item_2.display_price()
