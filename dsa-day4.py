# Given an array of integers, find the contiguous subarray with the  maximum sum 

def max_subarray(nums):
   max_sum = nums[0]
   current_sum = nums[0]
   for num in nums[1:]:
      current_sum = max(num, current_sum + num)
      max_sum = max( max_sum , current_sum )
   return max_sum



# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))  # Output: 6 (subarray [4, -1, 2, 1])