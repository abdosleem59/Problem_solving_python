# O(N^2)
lst = list(map(int, input().split()))
slide_window_num = int(input())

mx_sum = None
left_ptr =0
right_ptr = slide_window_num
for idx in range(len(lst)):
    sublist_sum = sum(lst[left_ptr:right_ptr])

    if mx_sum == None or mx_sum < sublist_sum:
        mx_sum = sublist_sum

    if left_ptr<len(lst) - slide_window_num:
        left_ptr +=1
    if right_ptr<len(lst):
        right_ptr +=1

print(mx_sum)

##############################################
# O(N)
lst = list(map(int, input().split()))
slide_window_num = int(input())
pre_lst = []
sum = 0
# create a new lst with sum of the item and the previous items
for item in lst: # [9,2,6] ==> [9,11,17]
    sum += item
    pre_lst += [sum]

mx = pre_lst[slide_window_num-1] 
for idx in range(slide_window_num , len(lst)):
    window = pre_lst[idx] - pre_lst[idx - slide_window_num]
    mx = max(mx, window)

print(mx)

###############################################

# O(N)
lst = list(map(int, input().split()))
slide_window_num = int(input())

window  = sum(lst[:slide_window_num])
max_sum = window

for idx in range(slide_window_num, len(lst)):
    window = window - lst[idx - slide_window_num] + lst[idx]

    if max_sum < window:
        max_sum = window

print(max_sum)


###############################################
