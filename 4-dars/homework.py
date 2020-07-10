# Kiritilgan sonni oxirgi raqamini topish
# def qoldiq_son(a):
#     qoldiq = a % 10
#     return qoldiq

# a = int(input('a = '))
# print(f'{a} ning oxirgi raqami {qoldiq_son(a)} ga teng' )




# Kiritilgan sonni juft yoki toq ekanligini topish.
# def toq_son(a):
#     if a % 2 == 0:
#         print(f' {a} bu juft son')
#     else:
#         print(f' {a} bu toq son')   

# a = int(input('a = '))
# toq_son(a)


# 계산기
# def qushish(a, b):
#     return a + b

# def aytirish(a, b):
#     return a - b

# def kupaytirish(a, b):
#     return a * b

# def bulish(a, b):
#     return a // b
    
# a = int(input('a = '))
# amal = (input('+, -, *, /  = '))
# b = int(input('b = '))

# if amal == "+":
#     print(f'{a} + {b} = {qushish(a,b)}')
# elif amal == "-":
#     print(f'{a} - {b} = {aytirish(a,b)}')
# elif amal == "*":
#     print(f'{a} * {b} = {kupaytirish(a,b)}')
# elif amal == "/":
#     print(f'{a} : {b} = {bulish(a,b)}')



# Kiritilgan sonni oxirgi 2 raqamini topish
# def qoldiq_son(a):
#     return a%100

# a = int(input('a = '))
# qoldiq = qoldiq_son(a)
# if qoldiq == 0:
#     print(f'{a} sonning oxirgi raqami 00 ga teng!')
# else:
#     print(f'{a} ning oxirgi 2 raqami {qoldiq_son(a)} ga teng' )