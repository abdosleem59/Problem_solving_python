# Problem: Find the mountains
## Read a matrix. Print all positions that are a mountain.
### Position (r,c) is mountain if its value > 8 neighbours in the matrix

def get_neibghours(i,j, cnt=4):
    di = [-1,-1,-1,0,0,1,1,1]
    dj = [-1,0,1,-1,1,-1,0,1]
    return [(i+di[d], j+dj[d]) for d in range(cnt) if i+di[d] >=0 and j+dj[d]>=0]

# Reading the matrix
rows = int(input())
lst_of_lsts = [0] * rows

for row in range(rows):
    lst_of_lsts[row] = list(map(int, input().split()))

## Filter mountain or not
lst_res = []
for i, lst in enumerate(lst_of_lsts):
    for j, item in enumerate(lst):
        is_mountain = True
        for idx in get_neibghours(i,j,8):
            r,c =idx
            if r>rows -1 or c>rows-1:
                continue
            if item<lst_of_lsts[r][c]:
                is_mountain = False
                break
        if is_mountain:
            lst_res.append((i,j))

print(lst_res)
        
