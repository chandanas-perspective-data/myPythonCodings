def recursive_binary_search(search_list, value):
    # search list is a list of (value, index)
    if not search_list or (len(search_list) == 1 and search_list[0][0] != value):
        raise ValueError("Not found")
    if search_list[0][0] == value:
        return search_list[0][1]
    mid_idx = len(search_list)//2
    if search_list[mid_idx][0] <= value:
        return recursive_binary_search(search_list[mid_idx:], value)
    else:
        return recursive_binary_search(search_list[:mid_idx], value)

def find(search_list, value):
    return recursive_binary_search([ (x,i) for i,x in enumerate(search_list)], value)


print(find([1,2,3,4,5,6],6))