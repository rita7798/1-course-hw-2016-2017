print ("Является ли c решением линейного уравнения ax + b = 0?")
a = int(input ("a = "))
b = int(input ("b = "))
c = int(input("c = "))
if a * c + b == 0:
    print('Да')
else:
    print('Нет')
