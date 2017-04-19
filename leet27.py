class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        
        
        for idx in xrange(len(nums)):
            if nums[idx] != val:
                nums[count] = nums[idx]
                count+=1
        return count
            
