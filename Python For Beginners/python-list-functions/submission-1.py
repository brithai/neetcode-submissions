from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum_check = 0
    for num in nums:
        sum_check += num
    
    return sum_check

def get_min(nums: List[int]) -> int:
    min_val = min(nums)

    min_check = nums[0]
    for num in nums:
        if num < min_check:
            min_check = num

    if min_val == min_check:
        return min_check
    else:
        return None

def get_max(nums: List[int]) -> int:
    max_val = max(nums)

    max_check = nums[0]
    for num in nums:
        if num > max_check:
            max_check = num

    if max_val == max_check:
        return max_check
    else:
        return None

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
