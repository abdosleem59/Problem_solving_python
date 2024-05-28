# Problem: Pair of numbers
# Description: Read 3 integers N, M, SUM
# Find total number of pairs that satisfy 
# A + B == SUM where 
# 1 <= A <= N  and 1 <= B <= M

# Brute force solution: O(n*n)
'''
n,m,sum = map(int, input().split())
cnt =0

for i in range(1, n+1):
    for j in range(1, m+1):
        if i+j == sum:
            cnt+=1

print(cnt)
'''
##############################################
# Creative solution: O(n)
'''
n,m,sum = map(int, input().split())
cnt =0

for i in range(1, n+1):
    j = sum - i
    if j <= m and j >=1:    
        cnt+=1

print(cnt)
'''
###############################################
# a more creative solution that takes much less time and space: O(1)

n, m, sum = map(int,input().split())

res = None
# Case#1 
if sum>n+m:
    res = "There are no pairs"
# Case#2
elif sum==n+m:
    res = 1

else:
    # Case#3 Like: 70 70 70 OR Like: 200 300 70
    if n >= sum and m >= sum:
        res = sum-1
    
    # Case#4 Like: 50 60 70 OR 60 50 70
    elif n < sum and m < sum:
        if n>=m:
            res = m - (sum - n) + 1
        else:
            res = n - (sum - m) + 1

    # Case#5 Like 40 80 70 OR 80 40 70 OR 50 70 70
    elif n < sum or m < sum:
        if n>=sum:
            res = m
        elif m>=sum:
            res = n

print(res)
