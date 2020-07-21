a = int(input('Enter a = '))
b = int(input('Enter b = '))
c = int(input('Enter c = '))
minimum = a

if minimum > b and c>b:
    minimum = b
elif minimum > c and b > c:
    minimum = c
else:
    minimum = a

print(f'Minumum number is {minimum}')