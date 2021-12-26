from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, lg, ln

def check_input1(i):
    try:
        i = int(i)
    except ValueError:
        return False

    return True


def check_input2(i):
    try:
        i = int(i)
    except ValueError:
        return False
    
    if i > 0:
        return True
    if i <= 0:
        return False
    
def check_input_base(i):
    try:
        i = int(i)
    except ValueError:
        return False
    
    if i > 0 and i != 1:
        return True
    else:
        return False

def main():
    arr = ['exp2', 'exp3', 'root2', 'root3', 'fact', 'log', 'lg', 'ln']
    print("Доступні функції:")
    for i in arr:
        print(i, end=' ')
    print()
    while True:
        func = input("Введіть ім'я ф-ї , яку хочете використати або щось інше для виходу: ")
        if func in arr:
            if func == "exp2" or func == 'exp3':
                while True:
                    n = input("Введіть число: ")
                    if check_input1(n) == True:
                        break
                n = int(n)
                if func == 'exp2':
                    print(exp2(n))
                else:
                    print(exp3(n))
            if func == 'lg' or func == 'ln':
                while True:
                    n = input("Введіть число: ")
                    if check_input2(n) == True:
                        break
                n = int(n)
                if func == 'lg':
                    print(lg(n))
                else:
                    print(ln(n))
            if func == "log":
                while True:
                    a = input("Введіть основу логарифма: ")
                    b = input ("Введіть число: ")
                    if check_input_base(a) == True and check_input2(b) == True:
                        break
                a = int(a)
                b = int(b)
                print(log(a, b))
                
            if func == "root2":
                while True:
                    n = input("Введіть число: ")
                    if check_input2(n) == True:
                        break
                n = int(n)
                print(root2(n))  
            if func == "root3":
                while True:
                    n = input("Введіть число: ")
                    if check_input1(n) == True:
                        break
                n = int(n)
                print(root3(n))            
            if func == 'fact':
                while True:
                    n = input("Введіть число: ")
                    if check_input2(n) == True:
                        break
                n = int(n)
                print(fact(n))
        else:
            break 
        

if __name__ == '__main__':
    main()