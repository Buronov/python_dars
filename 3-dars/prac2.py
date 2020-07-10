#Quyida 5 raqamli shariklar bor. O'quvchi ularni qaramasdan olib shunday ajratmoqchi.
#     1.Agar olgan sharikning raqami juft son bo'lsa sharikni sariq rangga bo'yamoqchi.
#     2. Agar olgan sharikning raqami toq son bo'lsa sharikni qizil rangga bo'yamoqchi.
# va oxirida bo'yalgan sariq va qizil sharikchalarni soni qaysi biri ko'pligini topmoqchi.
#programma: 5 ta son kiritiladi va qaysi rangdagi sharlar ko'pligi aniqlansin.

a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
c = int(input("Uchunchi son: "))
d = int(input("To'rtimchi son: "))
e = int(input("Beshinchi son: "))
# sharik = a

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0 and e % 2 == 0:
    print("Sariqga bo'yaysiz")
else:
    print("Qizil rangga bo'yaysiz")
