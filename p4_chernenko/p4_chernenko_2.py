#task 2
magnitude = input()
if magnitude < 2:
    print("Micro")
elif magnitude >= 2 and magnitude < 3:
    print("Very minor")
elif magnitude >= 3 and magnitude < 4:
    print("Minor")
elif magnitude >= 4 and magnitude < 5:
    print("Light")
elif magnitude >= 5 and magnitude < 6:
    print("Moderate")
elif magnitude >= 6 and magnitude < 7:
    print("Strong")
elif magnitude >= 7 and magnitude < 8:
    print("Major")
elif magnitude >= 8 and magnitude < 10:
    print("Great")
else:
    print("Meteoric")