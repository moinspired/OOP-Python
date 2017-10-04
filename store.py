#store to contain our products by making a store class and putting our products into an array.
#Autor: MOtuma Ayana
#10/04/2017

class Store(object):
    def __init__(self,location, owner):
        self.product = []
        self.location = owner
        self.owner = owner

    # add a product to the store's product list
    def add_product(self, a):
        self.product.append(a)
    # remove a product according to the product name
    def remove_product(self, name):
        temp  = []
        for i in self.product:
            if i == name:
                continue;
            else:
                temp.append(i)
        self.product = temp
        return self.product
    # print relevant information about each product in the store
    def inventory():
        pass
    def __str__(self):
        inventory = ""
        inventory += "Products:" + str(self.product) + "\n"
        inventory += "Location:" + self.location + "\n"
        inventory += "Owner:" + self.owner
        return inventory

store1 = Store("Silver Sprint", "Motuma")
store1.add_product('shoes')

store1.add_product('car')
store1.add_product('water')

store1.remove_product('car')


print store1
