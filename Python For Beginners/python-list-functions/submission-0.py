from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    output = 0

    for i in range(len(nums)):
        output += nums[i]
    
    return output

def get_min(nums: List[int]) -> int:
    curr_min = float('inf')

    for i in range(len(nums)):
        if nums[i] < curr_min:
            curr_min = nums[i]
    
    return curr_min

def get_max(nums: List[int]) -> int:
    max_num = float('-inf')

    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
    
    return max_num

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
