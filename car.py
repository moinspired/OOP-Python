class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print 'The price is: $' + str(self.price)
        print 'The speed is: ' + str(self.speed) + 'MPH'
        print 'The fuel is: ' + self.fuel
        print 'Mileage: ' + str(105)
        print 'Tax: ' + str(self.tax)


car1 = Car(2000, 35, 'Full', 15)
car1.display_all()
