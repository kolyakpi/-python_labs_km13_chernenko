import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def sign(number_of_permut):
    """
    В цій функції рахується для кожної перестановки її знак + чи -. 
    """
    res_arr = []
    num_mist = []
    number_of_permutArr = list(number_of_permut)
    for perm in number_of_permutArr:

        counter = 0
        for i in range(len(perm)):

            num = int(perm[i])
            for k in perm[i+1:]:
                if num > int(k):
                    counter += 1
        num_mist.append(counter)

    
    for i in num_mist:
        if i % 2 == 0:
            res_arr.append("+")
        else:
            res_arr.append("-")

    return res_arr

def number_of_permut(number):
    '''
    В цій функції обчислюється кількість можливих перестановок для заданої
    розмірності матриці. На вхід приймає розмірність матриці.
    '''
    string = ""
    for i in range(number):
        string += str(i+1)
    result = list(itertools.permutations(string, number))
    return result

def dobutok(number_of_permut, matrix, N):
    """
    В цій функції обчислюється добуток відповідних елементів 
    матрциі. На вхід подається масив строк перестановок, многомірний масив ( матриця ), розмірність матриці 
    """
    result_arr = []
    for k in number_of_permut:
        first_ind = 0
        dobutok = 1
        for j in range(len(k)):
            dobutok *= matrix[first_ind][int(k[j])-1]
            first_ind += 1
        result_arr.append(dobutok)


    return result_arr

def summa(arr):
    """
    В цій функції сумуються отримані добутки з 
    урахуванням знаку. Приймає на вхід масив чисел
    """
    result = 0
    flag = 1
    signs = sign(number_of_permut)
    for i in range(len(arr)):
        if signs[i] == "+":
            result += arr[i]
        elif signs[i] == "-":
            result += (-1)*arr[i]
    return result

def check_input(i):
    """
    Функция проверяет целое и положительное ли число. На вход подается введенніе значения пользователем.
    """
    is_good = True
    
    next_check = True
    try:
        i = int(i)
    except ValueError:
        next_check = False

    if next_check == True:
        flag = True

        if int(i) < 0:
            flag = True
        else:
            flag = False

        if flag == True:
            is_good = False
        else:
            is_good = True
    else:
        is_good = False

    return is_good

while True:
    n = input("Введите размерность матрицы: ")
    if check_input(n) == True:
        break
    else:
        print("Вы имеете право вводить только целые положительные числа!!! Попробуте еще раз.")

#Проверка данных

n = int(n)
matrix = random_matrix(int(n))
print("Случайно сгенерированная матрица: ")
print(matrix)
number_of_permut = number_of_permut(n)
print("Определитель равен: ", summa(dobutok( number_of_permut, matrix, n)))

print("Для сравнения: ")
print("np.linalg.det(matrix): ", round(np.linalg.det(matrix)))








































