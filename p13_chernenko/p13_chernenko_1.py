#f = open('/home/kolya/Desktop/Studying/pythonHomeworks/p12_chernenko/gadsby.txt', 'r')
#З тим директорієм що вище в мене на наотбуці працювало
#з цим що нижче який я Вам встановлю не впвенеий що запрацює....
f = open('gadsby.txt', 'r')
dict = ["a", "b", "c", "d","e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v","w", "x", "y", "z"]
numb1 = []
for i in range(len(dict)):
    numb1.append(0)

counter = 0
for i in f:
    for k in i:
        if k.isalpha() == True:
            if k.lower() in dict:
                ind = dict.index(k.lower())
                numb1[ind] += 1
                counter += 1

numb = []
for i in range(len(numb1)):
    numb.append((numb1[i]*100)/counter)

mistake = 1
while True:
    mistake = 0
    for i in range(len(numb)):
        if i != 0:
            if numb[i] < numb[i-1]:
                number = numb[i]
                numb[i] = numb[i-1]
                numb[i-1] = number
                alpha = dict[i-1]
                dict[i-1] = dict[i]
                dict[i] = alpha
                mistake = 1
    if mistake == 0:
        break
    
for i in reversed(range(len(numb))):
    if i >= len(numb)-5 and i <= len(numb)-1:
        print("Буква: {0} , її процент: {1}".format(dict[i], round(numb[i], 3)))

print("....")

for i in reversed(range(len(numb))):
    if i >= 0 and i <= 4:
        print("Буква: {0} , її процент: {1}".format(dict[i], round(numb[i], 3)))










