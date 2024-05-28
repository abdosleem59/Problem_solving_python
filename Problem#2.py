# Problem: Triples of numbers
# Read integer N, M, W.
# Find the total number of triples that has A+B<=C where
# 1 <= A <= N
# A <= B <= M
# 1 <= C <= W

# Brute force solution: O(n*n*n)
'''
n, m, w = map(int,input().split())
cnt = 0
for a in range(1,n+1):
    for b in range(a, m+1):
        for c in range(1, w+1):
            if a+b<=c:
                cnt+=1
print(cnt)
'''
########################################

n, m, w = map(int,input().split())
cnt = 0
for a in range(1,n+1):
    for b in range(a, m+1):
        c = a + b
        if 1 <= c <= w:
            cnt+= w - c + 1

print(cnt)

