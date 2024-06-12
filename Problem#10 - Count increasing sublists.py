# Count increasing sublists of the llist
lst = list(map(int, input().split()))

idx_str = ''
if lst[0]<lst[1]:
    idx_str += '1' 
else:
    idx_str+='0'

for idx in range(1,len(lst)-1):
    if lst[idx+1]>=lst[idx]:
        idx_str+= '1'
    else:
        idx_str+= '0'

cnt = 0
res = len(lst)
for i in range(len(idx_str)-1,-1,-1):

    if idx_str[i] == '1':
        cnt+=1
        res+= cnt
    else:
        cnt = 0

print("Number of increasing subarrays=", res)
