from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    matches = 0
    for element in nums:
        if x == element:
            matches += 1
    return matches

# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
