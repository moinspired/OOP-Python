class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weigth = weight
        self.brand = brand
        self.cost = cost
        self.status = "For sale"

    def setChange(self):
        self.status = "SOLD"

    def addTax(tax):
        return self.price * tax

    def returns(reason):
        if reason == 'defected':
            self.status = 'defected'
            self.price = 0
        if reason == 'box':
            self.status = 'used'
            self.pice = price - (price * .20)

    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Item name: " + self.item_name
        print 'Weight: ' + str(self.weigth) + " Pound"
        print 'Brand: ' + self.brand
        print 'Cost: $' + str(self.cost)
        print 'Status: ' + self.status

product1 = Product(150,"shoes",5,"nike",20)
product1.setChange()
product1.displayInfo()
product1.returns('defected')
