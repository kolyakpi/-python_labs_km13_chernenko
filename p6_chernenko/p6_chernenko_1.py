string1 = input("input first string: ")
string2 = input("input second string: ")

arr1 = []
for i in string1:
    if i != " ":
        arr1.append(i.lower())

arr2 = []
for i in string2:
    if i != " ":
        arr2.append(i.lower())

count = 0
for i in arr2:
    if i in arr1:
        count += 1

if count < len(arr2):
    print("you are not able to form second string from first one")
elif count == len(arr2):
    print("you are able to form second string from first one!!!")
