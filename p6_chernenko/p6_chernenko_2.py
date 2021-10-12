arr1 = [".", ",", "?", "!", ":"]
arr2 = ["a", "b", "c"]
arr3 = ["d", "e", "f"]
arr4 = ["g", "h", "i"]
arr5 = ["j", "k", "l"]
arr6 = ["m", "n", "o"]
arr7 = ["p", "q", "r", "s"]
arr8 = ["t", "u", "v"]
arr9 = ["w", "x", "y", "z"]
arr0 = [" "]

str_input = input("input string: ")
arr_input = []
for i in str_input:
    if i != " ":
        arr_input.append(i.lower())
    elif i == " ":
       arr_input.append(" ") 

print(arr_input)

output = ""
for i in arr_input:
    if i.lower() in arr1:
        output += "1" * (arr1.index(i)+1)
    elif i.lower() in arr2:
        output += "2" * (arr2.index(i)+1)
    elif i.lower() in arr3:
        output += "3" * (arr3.index(i)+1)
    elif i.lower() in arr4:
        output += "4" * (arr4.index(i)+1)
    elif i.lower() in arr5:
        output += "5" * (arr5.index(i)+1)
    elif i.lower() in arr6:
        output += "6" * (arr6.index(i)+1)
    elif i.lower() in arr7:
        output += "7" * (arr7.index(i)+1)
    elif i.lower() in arr8:
        output += "8" * (arr8.index(i)+1)
    elif i.lower() in arr9:
        output += "9" * (arr9.index(i)+1)
    elif i.lower() in arr0:
        output += "0"
    else:
        pass

print(output)
    
    
    
    