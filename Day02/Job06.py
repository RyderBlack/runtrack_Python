class Order():
    def __init__(self, order_number):
        self.__order_number = order_number
        self.__ordered_dishes = {}
        self.__order_status = "in progress"

    def get_order_number(self):
        return self.__order_number

    def get_ordered_dishes(self):
        return self.__ordered_dishes

    def get_order_status(self):
        return self.__order_status



    def set_order_number(self, order_number):
        self.__order_number = order_number

    def set_order_status(self, status):
        if status in ["in progress", "completed", "cancelled"]:
            self.__order_status = status
        else:
            raise ValueError("Invalid order status")

    def complete_order(self):
        self.set_order_status("completed")

    def cancel_order(self):
        self.set_order_status("cancelled")
        
    def add_dish(self, dish_name, price):
        self.__ordered_dishes[dish_name] = {"price": price, "status": self.__order_status}
        
    def calculate_total(self):
        total = 0
        for dish in self.__ordered_dishes.values():
            total += dish["price"]
        return total
    
    def display_order(self):
        print(f"Order Number: {self.get_order_number()}")
        print("Ordered Dishes:")
        for dish_name, dish_info in self.__ordered_dishes.items():
            print(f"{dish_name}: ${dish_info['price']}")
        
        total_amount = self.calculate_total()
        vat = self.calculate_vat()
        total_with_vat = total_amount + vat
        
        print(f"Total Amount to be Paid (excluding VAT): ${total_amount:.2f}")
        print(f"VAT: ${vat:.2f}")
        print(f"Total Amount to be Paid (including VAT): ${total_with_vat:.2f}")
        
    def calculate_vat(self):
        vat_rate = 0.10
        total = self.calculate_total()
        vat = total * vat_rate
        return vat
        
order_011 = Order(11)
# print(order_011.get_order_number()) 

order_011.add_dish("Sushis", 17)
order_011.display_order()
