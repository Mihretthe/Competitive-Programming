class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name: {self.name}, age: {self.age}")

class Order(Customer):
    
    def __init__(self, name, age, price):
        super().__init__(name, age)
        self.price = price
    def display(self):
        print(f"name: {self.name}, age: {self.age} price: {self.price}")



order = Order(name='Pizza', age='20', price=30)
order.display()

3