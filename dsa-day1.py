
### Day 1: Arrays
**Question**: Given an array of integers, return the indices of the two numbers that add up to a specific target.
**Answer**:
###
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i
    return []
