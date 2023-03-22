x = 30
flag = True
for i in range(x+1):
    
    if flag:
        for j in range(x+1):
            if i == (x/2):
                print("*", end = '')
                if i == j:
                    flag = False

            elif j == ((x/2)+(i)) or j == ((x/2)-(i)):
                print("*", end = '')
            
            else:
                print(" ", end = '')
    else:
        for k in range(x):
            
            if k == ((x/2)+((i-x))) or k == ((x/2)-((i-x))):
                print("*", end = '')
            
            else:
                print(" ", end = '')  

    print()