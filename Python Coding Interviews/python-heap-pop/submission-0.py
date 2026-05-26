import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    popped_ele = []

    for _ in range(len(heap)):
        curr_ele = heapq.heappop(heap)
        popped_ele.append(curr_ele)
    
    return popped_ele


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
