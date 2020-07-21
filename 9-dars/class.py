


# class Book:
#     id_number = None
#     name = None
#     cost = None
#     year = None

#     def set_idnumber(self, id_number):
#         self.id_number = id_number

#     def set_name(self, name):
#         self.name = name

#     def set_cost(self, cost):
#         self.cost = cost

#     def set_year(self, year):
#         self.year = year

#     def get_idnumber(self):
#         return self.id_number

#     def get_name(self):
#         return self.name

#     def get_cost(self):
#         return self.cost

#     def get_year(self):
#         return self.year

# book = Book()
# book.id_number = 1
# book.name = 'Python'
# book.cost = '$10'
# book.year = 1998
# print(f'id number: {book.id_number}')
# print(f'name: {book.name}')
# print(f'cost: {book.cost}')
# print(f'year: {book.year}')
# print('************************************\n')
# # SET
# book.set_idnumber(2)
# book.set_name('java')
# book.set_cost('%25')
# book.set_year(1996)
# print(f'id number: {book.id_number}')
# print(f'name: {book.name}')
# print(f'cost: {book.cost}')
# print(f'year: {book.year}')
# print('************************************\n')
# # GET
# print(f'id number: {book.get_idnumber()}')
# print(f'name: {book.get_name()}')
# print(f'cost: {book.get_cost()}')
# print(f'year: {book.get_year()}')


# KONSTRUKTOR
class Book:
    def __init__(self, id_number, name, cost, year):
        self.id_number = id_number
        self.name = name
        self.cost = cost
        self.year = year
book = Book(id_number=1, name='Python', cost='$15', year=1998)
print(f'id number: {book.id_number}')
print(f'name: {book.name}')
print(f'cost: {book.cost}')
print(f'year: {book.year}')