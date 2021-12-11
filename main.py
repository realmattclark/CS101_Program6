class Store:
    def __init__(self):
        pass
    
    def set_name_location(self, name, location):
        self.name = name
        self.location = location
    
    def display(self):
        return 'Products as follows: \nMilk : $2.50 \nBread : $1.98 \nEggs : $.70 \nFlour : $1.18 \nOil : $4.00 \nCheese : $2.68'

class Cart(Store):
    def __init__(self):
        self.items = {}
        self.receipt = 0
        self.item_name = ''
        self.item_quantity = 0
    
    def product_price(self, product_price):
        self.product_price = product_price

    def add_item(self):
        self.item_name = input('Enter the name of the product : ')
        self.item_quantity = int(input('Enter the number of items'))
        print('User placed order from:', self.name, 'from', self.location, 'location.')

    def display(self):
        if (len(self.items)>0):
            print('Order in cart is :')
            for item in self.items:
                print(item, ' with quantity of', str(self.items[item]))
            print('Total receipt is : $',str(self.receipt))
        else:
            print('Cart is empty')

def main():
    remove = add = True
    cart = Cart()
    store = Store()
    name = input('Which store would you like to use today?')
    location = input('Which location would you like to use?')
    cart.set_name_location(name, location)
    print(store.display())
    
