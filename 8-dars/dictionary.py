# Dictionary
# dic = {'key':'value'}

student = {
    'first_name': 'Jonibek', # 'first_name' is key, 'Jonibek' is value.
    'last_name': 'Buronov',  # vergul (,) bilan ajratiladi.
    'age': 18,
    'university': 'SEOULTECH',
    'id': 29092002
}

# first_name = student['first_name']
# last_name = student['last_name']
# age = student['age']
# id = student['id']
# print(first_name)
# print(last_name)
# print(age)
# print(id)

# UPDATE
# print(student)
# student['university'] = 'KYEONGNAM'
# print(student)

# COPY()
# new_dict = student.copy()
# print(new_dict)



students = [
     {
    'first_name': 'Jonibek', 
    'last_name': 'Buronov',  
    'age': 18,
    'university': 'SEOULTECH',
    'id': 29092002
    },
    {
    'first_name': 'Qahhorov', 
    'last_name': 'Bekzod',  
    'age': 18,
    'university': 'KYEONGNAM',
    'id': 20010325
    },
    {
    'first_name': 'Eshmatov', 
    'last_name': 'Toshmat',  
    'age': 18,
    'university': 'QSHX',
    'id': 29092002
    }
]

print(students[1])  # index orqali chaqirish.

for i in students:
    print(i['university'])    # for function orqali key chaqirish.