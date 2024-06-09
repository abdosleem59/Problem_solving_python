# Problem: Find the index of the top 2 maximum value

'''
# Slow solution
lst = list(map(int, input().split()))

mx1 = lst[0]
idx1 = 0 
for i, item in enumerate(lst):
    if item>mx1:
        mx1 = item
        idx1 = i

lst.pop(idx1)
print(idx1)
mx2 = lst[0]
idx2 = 0 
for i, item in enumerate(lst):
    if item>mx2:
        mx2 = item
        idx2 = i
        
print(idx2)
'''

###############################################33
# Better & faster solution
lst = list(map(int, input().split()))

idx_max_val_1 = 0 
idx_max_val_2 = 0
for i, item in enumerate(lst):
    
    if item>lst[idx_max_val_1]:
        idx_max_val_2 = idx_max_val_1
        idx_max_val_1 = i

    # check if the index of 2nd max value is correct or not
    if item < lst[idx_max_val_1]:
        if lst[idx_max_val_2]<item:
            idx_max_val_2 = i
    
    

print(idx_max_val_1, idx_max_val_2)
