# Problem: Digits sum in range
## Read 3 integers N,A,B
## Print the summation of the numbers between 1 and N
## Whose sum of digits is between A and B

n, a, b = map(int,input().split())

sumall = 0
for num in range(1, n+1):
    sumOfDigits = 0
    num2 = num
    while num>0:
        sumOfDigits+=num % 10
        if sumOfDigits > b:
            break
        num//=10
        
    if sumOfDigits>=a and sumOfDigits<=b:
        sumall+=num2

print(sumall)
