


numbers = [9, 7, 6, 15 , 17 , 5, 10, 11]

def insertion_sort(in_list): 

    n = len(in_list)

    if n <= 1:
        return in_list

    for j in range(1, n): 
        key = in_list[j]
        i = j - 1 

        while i >= 0 and key < in_list[i]:
            in_list[i+1] = in_list[i]
            i -= 1 
        in_list[i+1] = key 

    return in_list

insertion_sort(numbers)


