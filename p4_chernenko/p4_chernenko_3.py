#task3
while True:
    input_numb = int(input())
    if input_numb < 0:
        print("You entered the number that is less than zero!!!")
    else:
        break
input_numb1 = input_numb

cost = 0
flag = True

counter = 0
while flag == True:
    counter += 1 
    if counter == 1:
        input_numb -= 50
        cost += 100
    elif counter == 2:
        input_numb -= 50
        cost += 50
    elif counter > 2:
        cost += input_numb * 2
        flag = False
    
    if input_numb <= 0:
        flag = False 

print("You are going to pay: ", cost, " , for ", input_numb1, " minutes talking via this operator!")