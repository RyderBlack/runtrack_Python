class Product:
    def __init__(self, name, priceHT, VAT):
        self.name = name 
        self.priceHT = priceHT 
        self.VAT = VAT / 100
        
    def calc_price(self):
        vat_amount = self.priceHT * self.VAT
        priceTTC = self.priceHT + vat_amount
        return priceTTC
    
    def change_product_name(self, new_product_name):
        self.name = new_product_name
        return f"The new product name is {self.name}"
    
    def change_product_price(self, new_priceHT):
        self.priceHT = new_priceHT
        total = self.calc_price()
        return f"The new price is {total}"
    
    
milk = Product("milk", 23, 20)
print(milk.calc_price())
        
apple = Product("apple", 3.5, 5.5)
print(apple.calc_price())   

cake = Product("cake", 17.99, 20)
print(cake.change_product_name("red velvet"))
print(cake.change_product_price(99))