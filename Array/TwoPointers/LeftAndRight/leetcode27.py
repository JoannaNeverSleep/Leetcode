'''27. Remove Element'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int

        Goal: Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
                The order of the elements may be changed. 
                return the number of elements in nums which are not equal to val.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            while nums[left] != val: left += 1
            while nums[right] == val: right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left