# INHERITANCE

class Product:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def quantity(self, quantity):
        return self.cost * quantity

class Apple(Product):

    def __init__(self, name, cost, color):
        super().__init__(name, cost)
        self.color = color

class Book(Product):

    def __init__(self, name, cost, year):
        super().__init__(name, cost)
        self.year = year

apple = Apple('apple', 2000, 'red')
book = Book('book', 100000, 2018)
print(f'Product name: {apple.name}')
print(f'Product cost: {apple.cost}')
print(f'Product color: {apple.color}')
print(apple.quantity(10))
print('****************************\n')
print(f'Product name: {book.name}')
print(f'Product cost: {book.cost}')
print(f'Product color: {book.year}')
print(book.quantity(10))