# Calculator

class Calculator:
    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two

    def add_number(self):
        return self.number_one + self.number_two

    def sub_number(self):
        return self.number_one - self.number_two

    def multipy_number(self):
        return self.number_one * self.number_two

    def div_number(self):
        return self.number_one // self.number_two

number_one = int(input('Enter number one = '))
number_two = int(input('Enter number two = '))
calculator = Calculator(number_one=number_one, number_two=number_two)
choice = input('Enter +, -, *, / : ')
if choice == '+':
    print(f'{number_one} + {number_two} = {calculator.add_number()}')
elif choice == '-':
    print(f'{number_one} - {number_two} = {calculator.sub_number()}')
elif choice == '*':
    print(f'{number_one} * {number_two} = {calculator.multipy_number()}')
elif choice == '/':
    print(f'{number_one} / {number_two} = {calculator.div_number()}')
else:
    print('Xatolik!')