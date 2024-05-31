# Problem: Count how many X, Y numbers such that
## X in range [50 - 300]
## Y in range [70 - 400]
### Where X<Y and (X+Y) divisible by 7

#############################################

## First solution (Normal solution)
cnt=0
loops =0 
for x in range(50,301):
    for y in range(70,401):
        loops+=1
        if x<y and (x+y)%7==0:
            cnt+=1

print(cnt, loops)

################################################

## Second solution:
## Let's speed it, we can alwayse start from maximum of(70, x+1)
## this solution saves some Y iterations, and remove the X<Y condition
'''
cnt=0
for x in range(50,301):
    start= max(70, x+1)
    for y in range(start,401):
        if (x+y)%7==0:
            cnt+=1

print(cnt)
'''
###############################################

## Third solution:
## Let's speed it more, we can start by adding smallest values of X and Y then move 7 steps every time.
## this solution saves a lot of iterations and calculate value of Y by substract sum - x
'''
cnt=0
for num in range(126,701,7):
    for x in range(50, 301):
        y = num - x
        if 70 <= y <= 400 and x < y:
            cnt+=1

print(cnt)
'''
