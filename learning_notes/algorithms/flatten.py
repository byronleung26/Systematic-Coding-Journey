def flatten(lst):
    new_lst = []
    if len(lst)  <= 1:
        new_lst.append(lst[0])
    else:
        flatten(lst[1:])
    return new_lst
    

lst = [1, [2, [3, 4], 5], 6, [7, 8]]
print(flatten(lst))