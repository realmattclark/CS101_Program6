class Store:
    def __init__(self):
        pass
    
    def set_name_location(self, name, location):
        self.name = name
        self.location = location
    
    def display(self):
        return 'Products available: \nMilk : $2.50 \nBread : $1.98 \nEggs : $.70 \nFlour : $1.18 \nOil : $4.00 \nCheese : $2.68'

class Cart(Store):
    def __init__(self):
        self.item = {}
        self.receipt = 0
        self.item_name = ''
        self.item_quantity = 0
    
    def product_price(self, product_price):
        self.product_price = product_price

    def add_item(self):
        self.item_name = input('Enter the name of the product : ')
        self.item_quantity = int(input('Enter the number of items'))
        print('User placed order from:', self.name, 'from', self.location, 'location.')
        if(self.product_price.get(self.item_name, '')!=''):
            if(self.item_name(self.item_name, '')!=''):
                self.items[self.item_name] += self.item_quantity
            else:
                self.items[self.item_name] = self.item_quantity
            if str(self.product_price.get(self.item_name, '')!=''):
                self.receipt += (self.product_price[self.item_name] * self.item_quantity)

        else:
            pass

    def remove_item(self):
        if (len(self.item_quantity)>0):
            self.productname = input('Enter name of product to remove :\n')
            self.item_quantity = int(input('Enter amount to remove : \n'))
            print('User placed order from : ',self.name, 'at :', self.location)
            if(self.items.get(self.item_name,'')!=''):
                self.items[self.item_name] -= self.item_quantity
                if(self.items[self.item_name] <= 0):
                    del self.items[self.item_name]

                if(self.product_price.get(self.item_name, '')!=''):
                    self.receipt -= (self.product_price[self.item_name] * self.item_quantity)
        else:
            print('Cart is empty')
            pass


    def display(self):
        if (len(self.items)>0):
            print('Order in cart is :')
            for item in self.items:
                print(item, ' with quantity of', str(self.items[item]))
            print('Total receipt is : $',str(self.receipt))
        else:
            print('Cart is empty')

def main():
    add = remove = True
    cart = Cart()
    store = Store()
    name = input('Which store would you like to use today?')
    location = input('Which location would you like to use?')
    cart.set_name_location(name, location)
    print(store.display())
    cart.product_price({'Milk':2.5, 'Bread':1.98, 'Eggs':.70, 'Flour':1.18, 'Oil':4.00, 'Cheese':2.68})
    cart.add_item()
    cart.display()
    while remove == True or add == True:
        if input('\nDo you want to remove an item? (Y/N)\n/'.lower() == 'y'):
            remove = True
            cart.remove_item
            cart.display()
        else:
            remove = False
        
        if input('\nDo you want to add another item to cart? (Y/N)\n'.lower() == 'y'):
            add = True
            cart.add_item()
            cart.display()
        else:
            add = False
    
if __name__ == '__main__':
    main()