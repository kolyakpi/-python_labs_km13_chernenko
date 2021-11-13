import numpy as np

years = np.arange(1900, 2020+1, 1)

def function(years):
    vusokos = list(filter(lambda i: i % 400 == 0, years))
    years = list(set(years) - set(vusokos))
    
    NEvusokos = list(filter(lambda i: i % 100 == 0, years))
    years = list(set(years) - set(NEvusokos))
    
    vusokos += list(filter(lambda i: i % 4 == 0, years))
    years = list(set(years) - set(vusokos))
    
    NEvusokos += years

    return vusokos

def num_month(function, month, year):
    one = [1, 3, 5, 7, 8, 10, 12]
    zero = [4, 6, 9, 11]
    arr = [int(year)]
    
    if int(month) in one:
        print("В этом месяце этого года " + str(31) + " день.")
    elif int(month) in zero:
        print("В этом месяце этого года " + str(30) + " дней.")
    elif int(month) == 2:
        vusokos = function(arr)
        if len(vusokos) != 0:
            print("В этом месяце этого года " + str(29) + " дней.")
        else:
            print("В этом месяце этого года " + str(28) + " дней.")

def check_input(i, flag):    
    if flag == 1 and len(i) != 4:
        return False
    
    try:
        i = int(i)
    except ValueError:
        return False

    if int(i) < 0:
        return False

    if flag == 0 and int(i) > 12:
        return False
    
    if flag == 3 and (int(i) != 1 and int(i) != 2):
        return False

    return True

def first_func():
    while True:
        month = input("Введите номер месяца: ")
        if check_input(month, 0) == True:
            break
        else:
            print("Некорректные данные. Попробуйте еще раз")
    while True:
        year = input("Введите год: ")
        if check_input(year, 1) == True: 
            break
        else: 
            print("Некорректные данные. Попробуйте еще раз")
    num_month(function, month, year)


while True:
    flag = input("Для проверки первого задания введите 1, для второго введите 2: ")
    if check_input(flag, 3) == True:
            break
    else:
        print("Некорректные данные. Попробуйте еще раз")
flag = int(flag)
if flag == 1:
    print('Результат: ')
    print(function(years))
elif flag == 2:
    first_func()
    





































