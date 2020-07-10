students = [
     {
    'first_name': 'Jonibek', 
    'last_name': 'Buronov',  
    'age': 18,
    'university': 'SEOULTECH',
    'id': 'j29092002'
    },
    {
    'first_name': 'Bekzod', 
    'last_name': 'Qahhorov',  
    'age': 19,
    'university': 'KYEONGNAM',
    'id': 'b20010325'
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

def student_remove(id):
    for i in students:
        if i['id'] == id:
            students.remove(i)

print(students)
print('After removing a new student\n')
print(student_remove('j29092002'))
print(students)  # Bye Jonibek.