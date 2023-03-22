x = 30
flag = True
for i in range(int(x/2)+1):
    

    for k in range(1,x):
        if i == 0:
            print("*", end = '')
        elif k == ((x/2)+((i-(x/2)))) or k == (x/2)-((i-(x/2))):
            print("*", end = '')
        
        else:
            print(" ", end = '')  

    print()