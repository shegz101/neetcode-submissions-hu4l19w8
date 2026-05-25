from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    new_list = []

    i = 0
    original_len = len(arr)

    while i < original_len:
        new_list.append(arr[-1])
        arr.pop()
        i += 1
    
    return new_list


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
