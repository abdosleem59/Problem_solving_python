# Problem: Is it a prime or not.
n = int(input())

res=None
if n == 1:
    res = "NO"
elif n == 2:
    res = "Yes"
elif n % 2 == 0:
    res = "NO"
else:
    for i in range(3, n, 2):
        if n % i == 0:
            res = "NO"
            break

if res == None:
    print("YES")
else:
    print(res)
