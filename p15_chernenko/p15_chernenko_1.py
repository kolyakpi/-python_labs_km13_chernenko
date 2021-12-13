import math
def check_input(i):
    try:
        i = int(i)
    except ValueError:
        return False
    if int(i) < 0:
        return False
    else:
        return True 
while True:
    n = input("Введите степень многочлена: ")
    if  check_input(n) == True:
        break
n = int(n) + 1
a = [ [str(int(math.factorial(k)/(math.factorial(i)*math.factorial(k-i))))  for i in range(0, k+1)]  for k in range(0, n)]
for i in a:
    v = " ".join(i)
    print(v)