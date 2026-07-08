from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum_check = 0
    for num in nums:
        sum_check += num
    
    return sum_check

def get_min(nums: List[int]) -> int:
    min_check = nums[0]
    for num in nums:
        if num < min_check:
            min_check = num

    return min_check

def get_max(nums: List[int]) -> int:
    max_check = nums[0]
    for num in nums:
        if num > max_check:
            max_check = num

    return max_check

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
