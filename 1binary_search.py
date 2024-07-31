
def binary_search(list, mid, searched_num):
    low = 0
    high = len(list)
    while searched_num in list:
        if mid == None:
            mid = low + high/2
            round(mid)
        else:
            mid = round(mid)
            if list[mid] == searched_num:
                return searched_num, list.index(searched_num)

            if list[mid] > searched_num:
                mid = mid - 1
                binary_search(list, mid, searched_num)
            if list[mid] < searched_num:
                mid = mid + 1
                binary_search(list, mid, searched_num)


sorted_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
midd = None
secret_num = sorted_list[1]
print(binary_search(sorted_list, midd, secret_num))
