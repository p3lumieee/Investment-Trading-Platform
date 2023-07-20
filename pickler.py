class ShoppingSystem:
    def __init__(self):
        self.basket = []

    def add_item(self, item):
        self.basket.append(item)

    def remove_item(self, item):
        if item in self.basket:
            self.basket.remove(item)

    def show_basket(self):
        return self.basket
