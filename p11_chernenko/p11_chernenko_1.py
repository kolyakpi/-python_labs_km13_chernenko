# ВАШ КОД ТУТ

def cons(head, tail=[]):
    head = [head]
    result = head + tail
    return result 

# ПЕРЕВІРКА

l = cons(3, cons(2, cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

# ВАШ КОД ТУТ

def sum(arr):
    summa = 0
    if len(arr) == 1:
        return arr[0]
    else:
        summa += arr[0] + sum(arr[1:])
        return summa

#ПЕРЕВІРКА

print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')





































