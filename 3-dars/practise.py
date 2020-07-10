topshiriq = input("Birinchi bor o'qishga topshirmoqdamisiz? (ha yoki yo'q)\n")
if topshiriq=='ha':
    age = int(input('Yoshingiz:\n'))
    fname = input('Ismingiz: \n')
    lname = input('Familyangiz: \n')
    full_name = fname + " " + lname
    phone_number = int(input("Telefon raqamingiz:\n"))
    print('*****************************')
    print(f'Sizning ismingiz {full_name}')
    print(f'Sizning yoshingiz {age}')
    print(f'Sizning telefon raqamingiz {phone_number}')
    print("Siz to'lov qilmaysiz !")

elif topshiriq == "yo'q":
    person = input('ayol yoki erkak:\n')
    if person == 'erkak':
        age = int(input('Yoshingiz:\n'))
        if age > 17 and age < 30:
            # print("Siz 101 ming so'm to'lov qilishingiz kerak")
            fname = input('Ismingiz: \n')
            lname = input('Familyangiz: \n')
            full_name = fname + " " + lname
            phone_number = int(input("Telefon raqamingiz:\n"))
            print('*****************************')
            print(f'Sizning ismingiz {full_name}')
            print(f'Sizning yoshingiz {age}')
            print(f'Sizning telefon raqamingiz {phone_number}')
            print("Siz 101 ming so'm to'lov qilishingiz kerak")
        elif age > 30:
            # print("Siz 202 ming so'm to'lov qilishingiz kerak")
            fname = input('Ismingiz: \n')
            lname = input('Familyangiz: \n')
            full_name = fname + " " + lname
            phone_number = int(input("Telefon raqamingiz:\n"))
            print('*****************************')
            print(f'Sizning ismingiz {full_name}')
            print(f'Sizning yoshingiz {age}')
            print(f'Sizning telefon raqamingiz {phone_number}')
            print("Siz 202 ming so'm to'lov qilishingiz kerak")

    elif person == 'ayol':
        age = int(input('Yoshingiz:\n'))
        if age > 17 and age < 30:
            # print("Siz 81 ming so'm to'lov qilishingiz kerak")
            fname = input('Ismingiz: \n')
            lname = input('Familyangiz: \n')
            full_name = fname + " " + lname
            phone_number = int(input("Telefon raqamingiz:\n"))
            print('*****************************')
            print(f'Sizning ismingiz {full_name}')
            print(f'Sizning yoshingiz {age}')
            print(f'Sizning telefon raqamingiz {phone_number}')
            print("Siz 81 ming so'm to'lov qilishingiz kerak")
        elif age > 30:
            # print("Siz 150 ming so'm to'lov qilishingiz kerak")
            fname = input('Ismingiz: \n')
            lname = input('Familyangiz: \n')
            full_name = fname + " " + lname
            phone_number = int(input("Telefon raqamingiz:\n"))
            print('*****************************')
            print(f'Sizning ismingiz {full_name}')
            print(f'Sizning yoshingiz {age}')
            print(f'Sizning telefon raqamingiz {phone_number}')
            print("Siz 150 ming so'm to'lov qilishingiz kerak")