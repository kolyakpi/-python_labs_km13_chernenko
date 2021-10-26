import math

flag = True
while flag == True:
    flag = False
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")

    try:
        a = float(a)
    except ValueError:
        print("Ви ввели не число в 'a'. Введіть знову всі коефіцієнти")
        flag = True
    
    try:
        b = float(b)
    except ValueError:
        print("Ви ввели не число в 'b'. Введіть знову всі коефіцієнти")
        flag = True

    try:
        c = float(c)
    except ValueError:
        print("Ви ввели не число в 'c'. Введіть знову всі коефіцієнти")
        flag = True

#ax^2 + bx + c = 0

a = float(a)
b = float(b)
c = float(c)

descriminant = pow(b, 2) - 4*a*c

try:
    x1 = 0
    try:
        x1 = ( (-1)*b + math.sqrt(descriminant)) / (2 * a)
    except ValueError: 
        print("детермінант менше нуля.")
        x1 = ""
except ZeroDivisionError:
    print('а дорівнює нулю, неможливо знайти коренів, використовуючи формулу детермінанта.')
    x1 = ""

try:
    x2 = 0
    try:
        x2 = ( (-1)*b - math.sqrt(descriminant)) / (2 * a)
    except ValueError: 
        print("детермінант менше нуля.")
        x2 = ""
except ZeroDivisionError:
    print('а дорівнює нулю, неможливо знайти коренів, використовуючи формулу детермінанта.')
    x2 = ""
zero_sol = 0

print("x1", x1)
print("x2", x2)
if x1 == "" and x2 == "":
    zero_sol = 1
    raise Exception('Нема коренів')

if zero_sol == 0:
    if x1 != x2:
        print("x1: ", x1)
        print("x2: ", x2)
    else:
        print("x: ", x1)