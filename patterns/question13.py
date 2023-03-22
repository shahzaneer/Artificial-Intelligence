x = 30
for i in range(x):
    j = 0
    while j < i:
        if i == x-1:
            print("*", end = '')
        elif j == 0 or j == i-1:
            print("*", end = '')
        else:
            print(" ", end = '')
        j = j+1
 
    print()

j = x
while j > 0:
    for k in range(j-2):
        if k==0 or k == j-3:                        
            print("*", end = '')
        else:
            print(" ", end = '')
    j = j-1
    print()