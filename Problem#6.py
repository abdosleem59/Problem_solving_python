# Print all prime numbers from 1 to n
n = int(input())

res=None
if n == 1:
    print("There is no prime numbers")
elif n == 2:
    print(2)
else:
    print(2)
    for num in range(3, n+1, 2):
        flag = True
        for i in range(3,num,2):
            if num % i == 0:
                flag = False

        if flag:
            print(num)
