from typing import List

def read_integers() -> List[int]:    
    nums = input().split(",")

    num_list = []
    for num in nums:
        num_list.append(int(num))

    return num_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
