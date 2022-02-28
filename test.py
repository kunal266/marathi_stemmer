import itertools

rect_array = [[63, 175, 190], [249, 271], [312, 326], [410, 417, 457, 460, 466],
[410, 457, 417, 460, 466], [410, 460, 417, 457], [457, 460], [457, 466, 460], [1,2,3]]

new_rect_array = []

for arr in rect_array:
    arr.sort()
    new_rect_array.append(arr)


new_rect_array.sort()
new_rect_array = list(num for num,_ in itertools.groupby(new_rect_array))

rmv_lst = []
for i in range(len(new_rect_array) - 1):
    for j in (i+1, len(new_rect_array) - 1):
        if set(new_rect_array[i]).issubset(set(new_rect_array[j])):
            rmv_lst.append(new_rect_array[i])
        elif set(new_rect_array[j]).issubset(set(new_rect_array[i])):
            rmv_lst.append(new_rect_array[j])

print(rmv_lst)

rmv_lst.sort()
rmv_lst = list(num for num,_ in itertools.groupby(rmv_lst))

print(rmv_lst)

for dup in rmv_lst:
    new_rect_array.remove(dup)

print(new_rect_array)
