from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, lg, ln

def main():
    arr = ['exp2', 'exp3', 'root2', 'root3', 'fact', 'log', 'lg', 'ln']
    while True:
        func = input("Введіть ім'я ф-ї , яку хочете використати або щось інше для виходу: ")
        if func in arr:
            if func == "exp2":
                
            elif func == "log" or func == 'lg' or func == 'ln':
                
            
        else:
            break 
    
if __name__ == '__main__':
    main()