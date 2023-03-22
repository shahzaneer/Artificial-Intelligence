x = 30
for i in range (x):
    for j in range(x):
        if x-j < i:
            print("*", end = '')
        else:
            print(" ", end = '')
    print()
for i in range (x):
    for j in range(x):
        if j > i:
            print("*", end = '')
        else:
            print(" ", end = '')
    print()