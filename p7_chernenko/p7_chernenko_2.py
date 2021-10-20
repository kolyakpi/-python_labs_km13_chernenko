while True:
    first = input("First number: ")
    second = input("First number: ")
    third = input("First number: ")

    if int(first) >= 0 and int(first) <= 255 and int(second) >= 0 and int(second) <= 255 and int(third) >= 0 and int(third) <= 255:
        break
    else:
        print("You inputted wrong values!!! TRY AGAIN")

def transformation_number(number):
    number = int(number)
    result_letters = []
    primar_num = int(number)

    letters = ["A", "B", "C", "D", "E"]

    while number > 0:
        numb = number % 16

        if numb >= 10:
            index = numb - 10
            result_letters.append(letters[index]) 
        else:
            result_letters.append(str(numb))

        number = number // 16

    if primar_num != 0 and len(result_letters) != 2:
        result_letters.append('0')

    if primar_num == 0 and len(result_letters) != 2: 
        result_letters.append('00')
    
    result = ""
    i = len(result_letters) - 1

    while i >= 0:

        result += result_letters[i]
        i -= 1

    return result

first_16 = transformation_number(first)
second_16 = transformation_number(second)
third_16 = transformation_number(third)

def put_altogether(first_16, second_16, third_16):

    string_result = ""
    string_result += first_16
    string_result += second_16
    string_result += third_16
    return string_result

print("Converted RGB with base of 10 to RGB with base 16: ", put_altogether(first_16, second_16, third_16))