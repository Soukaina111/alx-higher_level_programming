def search_replace(my_list, search, replace):
    new_list = my_list[:]
    size = len(my_list)
    for i in range(size):
        if my_list[i] == search:
            new_list[i] = replace
    return new_list
