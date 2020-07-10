# 1-misol

# numbers = [10, 24, 12, 46, 78, 44, 90]
# list_one = []
# list_two = []

# for i in numbers:
#     if i % 4 == 0:
#         list_one.append(i)
#     else:
#         list_two.append(i)

# print(numbers)
# print(f"4 ga bo'linadiganlar: {list_one}")
# print(f"4 ga bo'linmaydiganlar: {list_two}")

# 2-misol
# numbers = [10,5, 24, 12, 7, 46, 78, 44, 90,1,9,3543]
# juft_son = []
# toq_son = []

# for i in numbers:
#     if i % 2 == 0:
#         juft_son.append(i)
#     else:
#         toq_son.append(i)

# print(numbers)
# print(f"Juft sonlar: {juft_son}")
# print(f"Toq sonlar: {toq_son}")

# 3-misol
# numbers = [10, 5, 24, 12, 7, 46, 78, 44, 90, 1, 9, 3543]

# for i in range(0, len(numbers)):
#     if numbers[i] % 5 == 0:
#         numbers[i] = 6
        
# print(numbers)


















# 4-misol. Max va Min'ni aniqlash

# def max_number(my_list):
#     max_number = my_list[0]
#     for i in my_list:
#         if i > max_number:
#             max_number = i
#     return max_number

    
# def min_number(my_list):
#     min_number = my_list[0]
#     for i in my_list:
#         if i < min_number:
#             min_number = i
#     return min_number

# numbers = [12, 85, 15, 47, 65, 23, 98, 75, 33, 66, 74]
# print(f'Max number is {max_number(numbers)}')
# print(f'Min number is {min_number(numbers)}')