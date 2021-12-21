#8 sheets         16 pages

def dec(flag =True):
    def actual_decorator(func):
        def inner(*args, **kwargs):
            if flag == True:
                new_arr=[]
                small1 = []
                small2 = []
                arr = func(*args, **kwargs)
                counter = 0
                for i in arr:
                    for j in i:
                        small2.append(j)
                        counter += 1
                        if counter == 4:
                            counter = 0
                            small1.append(small2)
                            small2 = []
                    new_arr.append(small1)
                    small1=[]
                for i in new_arr:
                    print(i)
            else:
                arr = func(*args, **kwargs)
                for i in arr:
                    print(i)
        return inner
    return actual_decorator
    
    
def check_input(i):
    try:
        i = int(i)
    except ValueError:
        return False
    if int(i) < 0:
        return False
    else:
        if i % 16 == 0:
            return True 
    return False
    
@dec(flag=False)
def count_pages(n):
    arr_res = []
    n = int(n)
    arr = []
    print("Number of notebooks: ", n)
    for j in range(n):
        for i in range(1, 8, 2): 
            arr.append(16-i+1 + 16*j)
            arr.append(i + 16*j)
            arr.append(i+1 + 16*j)
            arr.append(16-i + 16*j)
        arr_res.append(arr)
        arr=[]
    return arr_res

while True:
    pages = input("Input number of pages: ")
    if check_input(pages) == True:
        break
pages = int(pages)
notebooks = int(pages / 16) 
        
count_pages(notebooks)
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         