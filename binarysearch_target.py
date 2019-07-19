""" Search for a target in a list that is already sorted """
# Question Credit: leetcode - return index if found else -1
"""
nums = [-1,0,3,5,9,12], target = 9
Output: 4
nums = [-1,0,3,5,9,12], target = 2
Output: -1
nums = [2,5], targer = 2
Output 0
nums = [5], target = -5
Output = -1
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 1:
            if target != nums[0]:
                return -1
            return 0
        if nums[-1] < target or nums[0] > target:
            return -1
        index = len(nums)/2
        while index <= len(nums) and index>=0:
            if nums[index] < target:
                if index <= len(nums):
                    if nums[index+1] >target:
                        return -1
                index += 1
            elif nums[index] > target:
                if index > 0:
                    if nums[index-1] < target:
                        return -1
                index -= 1
            elif nums[index] == target:
                return index
        return -1
                
        

