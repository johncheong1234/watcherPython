from typing import List 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i+1!=nums[i] and nums[i]>=0 and nums[i]<=len(nums):
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)