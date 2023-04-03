'''27. Remove Element'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int

        Goal: Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
                The remaining elements of nums are not important as well as the size of nums.
                return the number of elements in nums which are not equal to val.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow