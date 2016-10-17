print ("3. Даёт ли a остаток c при делении на b?")
a = int(input ("a = "))
b = int(input ("b = "))
c = int(input("c = "))
if a % b == c:
    print('Да')
else:
    print('Нет')


print ("4. Является ли c решением линейного уравнения ax + b = 0?")
a = int(input ("a = "))
b = int(input ("b = "))
c = int(input("c = "))
if a * c + b == 0:
    print('Да')
else:
    print('Нет')

