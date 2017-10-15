class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        cursum = 0
        minsum = 0
        
        for ele in nums:
            
            if cursum <0:
                cursum=0
            cursum+=ele
            maxsum = max(maxsum,cursum)
        return maxsum
            
        
