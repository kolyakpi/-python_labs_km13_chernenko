mast = ["diamonds", "clubs", "hearts", 'spades']
values1 = (str(i) for i in range(2,11))
values = ["A"] + list(values1) + ["J", "Q", "K"]
b = [ ( [k+" "+i for k in values] ) for i in mast ]
result = b[0] + b[1] + b[2]+ b[3]
result1 = iter(result)
for i in range(len(result)):
    print(next(result1))
print(next(result1))