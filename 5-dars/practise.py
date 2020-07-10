# 1-misol
# toq va juft son
# def check_num(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False

# a = int(input("a = "))
# b = int(input("b = "))
# juft_son = 0
# toq_son = 0

# for i in range(a, b + 1):
#     if check_num(i) == True:
#         juft_son = juft_son + 1
#         print(f'{i} bu son Juft son.')
#     else:
#         toq_son = toq_son + 1
#         print(f'{i} bu son Toq son')

# print(f'{juft_son} ta Juft son  bor {a} va {b} sonning orasida.')
# print(f'{toq_son} ta Juft son  bor {a} va {b} sonning orasida.')


# 2-misol. Tub son aniqlash

# def check_number(a):
#     b = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             b = b + 1
#     return b

# a = int(input('a =  '))
# if check_number(a) == 2:
#     print(f'{a} son tub son!')
# else:
#     print(f'{a} son tub emas')




#3-misol
# def check_number(a):
#     b = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             b = b + 1
#     return b

# n = int(input('Enter n = '))
# for i in range(2, n + 1):
#     if check_number(i) == 2:
#         print(f'{i} tub son')



# def sum_number(a, b):
#     sum_number = 0
#     for i in range(a, b + 1):
#         sum_number = sum_number + i
#     return sum_number

# a = int(input('Enter a = '))
# b = int(input('Enter b = '))
# print(f'Sum number = {sum_number(a,b)}')
#*************************************

# def mult_number(a, b):
#     mult_number = 1
#     for i in range(a, b+1):
#         mult_number = mult_number * i
#     return mult_number

# a = int(input('Enter a = '))
# b = int(input('Enter b = '))
# print(f'Mult number = {mult_number(a,b)}')
#*************************************

#4-misol
# def number_div(a):
#     sum_number = 0
#     for i in range(1, a):
#         if a % i == 0:
#             sum_number = sum_number + i
#     return sum_number

# n = int(input('Enter n = '))
# if number_div(n) == n:
#     print(f"{n} ha")
# else:
#     print(f"{n} yo'q")
