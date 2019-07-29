"""
Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once. Find this single element that appears only once.
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0]
        i = 0
        while i <= len(nums)-1:
            if len(nums)-i < 2:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 2
            
        
