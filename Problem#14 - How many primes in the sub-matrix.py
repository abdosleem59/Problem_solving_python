# Problem: How many primes in the sub-matrix
## Read a matrix. In next line, read integer Q, for Q queries.
### In the next lines: read queries: sr sj r c
### Each queries is a grid with top left (sr, sc) and #rows & #cols
### For each query, print how many prime numbers in the requested sub-matrix.

def read_matrix():

    rows = int(input())
    assert rows>0
    lst_of_lsts = [0] * rows

    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))

    return rows, len(lst_of_lsts[0]), lst_of_lsts

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False

    return True


rows, col, matrix = read_matrix()

# prerprocessing for know the prime numbers
# if it is prime put 1, else put 0
primes_lst =[0] * rows
for i, lst in enumerate(matrix):
    new_lst =[0] * col 
    for j, item in enumerate(lst):
        if is_prime(item):
            new_lst[j] = 1
        else:
            new_lst[j] = 0

    primes_lst[i]=new_lst

queries = int(input())



for q in range(queries):
    sr, sc,r,c = map(int, input().split())
    res = 0
    for i in range(r):
        for j in range(c):
            if primes_lst[i+sr][j+sc]==1:
                res+=1
    print("The number of prime numbers in the sub-matrix is:",res)
############################################################################
# The same solution, but in a pythonic way.

primes_lst = [[is_prime(value) for value in row] for row in matrix]

q = int(input())    # queries
while q > 0:
    total_primes = 0
    sr, sc, nr, nc = map(int, input().split())
    # iterate on rows: slice the range and sum it
    for r in range(sr, sr + nr):
        total_primes += sum(primes_lst[r][sc:sc + nc])
    print(total_primes)
    q -= 1


