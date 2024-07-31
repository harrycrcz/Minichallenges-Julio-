
def delete_dup(list, list_two):
    for i in list:
        if i not in list_two:
            list_two.append(i)
    return list_two


first_list = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
new_list = []

final_list = delete_dup(first_list, new_list)
print(final_list)
