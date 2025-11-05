class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes:", self.stock)

    def rentForBike(self, q):
        if q <= 0:
            print("Enter a positive value greater than zero.")
        elif q > self.stock:
            print("Enter a value less than available stock.")
        else:
            print("Total Price:", q * 100)
            self.stock -= q
            print("Bikes Left:", self.stock)


# Main program loop
obj = BikeShop(100)

while True:
    uc = int(input('''
1. Display Stock
2. Rent a Bike
3. Exit
Enter your choice: '''))

    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input("Enter the quantity: "))
        obj.rentForBike(n)
    elif uc == 3:
        print("Thank you for visiting! Come again.")
        break
    else:
        print("Invalid choice! Please try again.")
