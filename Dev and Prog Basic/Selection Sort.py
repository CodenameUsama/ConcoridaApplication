

numbers = [8, 4, 6, 9, 2, 3, 1]

# def insertion_sort(in_list):

#     n = len(in_list)

#     if n <= 1:
#         return in_list

#     for j in range(0, n):
#         for i in range ((j + 1), n):
#             if in_list[i] < in_list[j]:
#                 i = j
#         in_list[j] = in_list[min]

# insertion_sort(numbers)


def insertion_sort(in_list):

    sorted_list = []
    n = len(in_list)

    if n <= 1:
        return in_list
    
    for j in range(0, n-1): 
        num = min(in_list)
        sorted_list.append(num)
        in_list.remove(num)
    
    print(sorted_list)

insertion_sort(numbers)



