# List methods
# 1. append - list oxiridan qo'shish.
# 2. insert - .insert(index, 'qiymat') xoxlagan joydan index orqali qo'shish.
# 3. remove - listdan olib tashlash.
# 4. pop - lsitdan o'chiradi. indexsiz ishlatilsa oxiridan o'chiradi.
# 5. clear - listni tozalab beradi.
# 6. del - listdan index[] orqali o'chirib tashlash.
# 7. copy
# 8. add list
# 9. extend

# 1. append 
# programming_language = ['python', 'java', 'c++', 'php']
# print(len(programming_language))
# print(programming_language)
# programming_language.append('javascript')
# print('After appending the list\n')
# print(len(programming_language))
# print(programming_language)

# # 2. insert
# programming_language = ['python', 'java', 'c++', 'php']
# print(len(programming_language))
# print(programming_language)
# programming_language.insert(0, 'javascript')
# print('After inserting the list\n')
# print(len(programming_language))
# print(programming_language)

# 3. remove
# programming_language = ['python', 'java', 'c++', 'php']
# print(len(programming_language))
# print(programming_language)
# programming_language.remove('php')
# print('After removing the list\n')
# print(len(programming_language))
# print(programming_language)

# 4. pop
# programming_language = ['python', 'java', 'c++', 'php']
# print(len(programming_language))
# print(programming_language)
# ,programming_language.pop(1)
# print('Af,t.,.er poping the list\n')
# print(len(programming_language))
# print(programming_language)

# 5. clear
# programming_language = ['python', 'java', 'c++', 'php']
# print(len(programming_language))
# print(programming_language)
# programming_language.clear()
# print('After clearing the list\n')
# print(len(programming_language))
# print(programming_language)

# 6. del
# programming_language = ['python', 'java', 'c++', 'php']
# print(len(programming_language))
# print(programming_language)
# del programming_language[0]
# print('After clearing the list\n')
# print(len(programming_language))
# print(programming_language)

# 7. copy
# programming_language = ['python', 'java', 'c++', 'php']
# new_copy_list = programming_language.copy()
# print(new_copy_list)

# 8. add list
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 6, 8, 10]
# list3 = list1 + list2
# print(list3)

# 9. extend
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 6, 8, 10]
# list2.extend(list1)
# print(list2)


# practise - Juft va Toq sonlarga ajratish.
# numbers = [1, 2, 5, 6, 4, 9, 64, 5445, 58, 8, 66, 23,]
# juft_son = []
# toq_son = []

# for i in numbers:
#     if i % 2 == 0:
#         juft_son.append(i)
#     else:
#         toq_son.append(i)

# print(f'Juft sonlar guruhi {juft_son}')
# print(f'Toq sonlar guruhi {toq_son}')