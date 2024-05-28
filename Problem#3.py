n = int(input())

counter_above = n-2
cntounter_down = 2
cntounter_down2 = 1
for i in range(n):
    space1 = i * ' '
    space2 = counter_above * ' '
    counter_above-=2
    # above section of X:
    if i<n//2:
        print(space1 + '*' + space2 + '*')
    
    elif i == n//2:
        print(space1 + '*')
    # down section of X
    else:# i=6, cntounter_down=2
        space1 = (n-i-1) * ' '
        space2 = (cntounter_down2) * ' '
        print(space1 + '*' + space2 + '*')
        cntounter_down2+=2
    
        

    
    


