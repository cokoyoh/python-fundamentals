class ShoppingCart(object):
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self, item_name, quantity, price):
        self.total += quantity * price
        self.items[item_name] = quantity

    def remove_item(self, item_name, quantity, price):
        if self.items.get(item_name, 0) < quantity:
            self.total -= self.items.get(item_name, 0) * price
            self.items.pop(item_name)
        else:
            self.items[item_name] = self.items[item_name] - quantity
            self.total -= quantity * price

    def checkout(self, cash_paid):
        if cash_paid < self.total:
            return 'Cash paid not enough'

        return cash_paid - self.total


shopping_cart = ShoppingCart()
shopping_cart.add_item('biriani', 3, 50)
shopping_cart.add_item('rice', 1, 20)

print(shopping_cart.total)
print(shopping_cart.items)

shopping_cart.remove_item('rice', 3, 20)

print(shopping_cart.total)
print(shopping_cart.items)
print(shopping_cart.checkout(200))


class Shop(ShoppingCart):
    def __init__(self):
        ShoppingCart.__init__(self)
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1


shop = Shop()
print(shop.quantity)
print(shop.remove_item())
