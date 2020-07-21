students = [
     {
    'first_name': 'Jonibek', 
    'last_name': 'Buronov',  
    'age': 18,
    'university': 'SEOULTECH',
    'student_id': 'j29092002'
    },
    {
    'first_name': 'Bekzod', 
    'last_name': 'Qahhorov',  
    'age': 19,
    'university': 'KYEONGNAM',
    'student_id': 'b20010325'
    }
   
]

# APPEND - QO'SHISH.
# def student_append(first_name, last_name, age, university, id):
#     students.append({'first_name': first_name, 'last_name': last_name, 'age': age, 'university': university, 'id': id})
    
# print(students)
# print('After appending a new student\n')
# student_append('Toshmat', 'Eshmatov', 20, 'QSHX', 't29092002')
# print(students)

# REMOVE - OLIB TASHLASH.

# def student_remove(id):
#     for i in students:
#         if i['id'] == id:
#             students.remove(i)

# print(students)
# print('After removing a new student\n')
# print(student_remove('j29092002'))
# print(students)  # Bye Jonibek.



# Homework
def search(student_id):
    find_student = None
    for i in students:
        if i['student_id'] == student_id:
            find_student = i
    return find_student

student_id = input('Enter Student id: ')
first_name = search(student_id)['first_name']
last_name = search(student_id)['last_name']
age = search(student_id)['age']
university = search(student_id)['university']
student_id = search(student_id)['student_id']
print(f'First name: {first_name}')
print(f'Last name: {last_name}')
print(f'Age : {age}')
print(f'University: {university}')
print(f'Student id: {student_id}')

# Append method
def update(student_id, age):
    students = search(student_id)
    students['age'] = age
    return students

student_id = input('Enter student id: ')
new_age = input('Enter age: ')
print(update(student_id, new_age))
