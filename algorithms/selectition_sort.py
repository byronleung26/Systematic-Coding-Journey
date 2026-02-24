list = [165, 172, 158, 180, 169, 155, 58, 98, 402, 205, 306, 75.6, 65.7]
new_list = []

def fin_smallest(arr):
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] <= smallest:
            smallest = arr[i]
            index = i
    return index

current_list = list[:]
for i in range(len(current_list)):
    small_index = fin_smallest(current_list)
    new_list.append(current_list.pop(small_index))

print(new_list)