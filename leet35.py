class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arrlen = len(nums)
        if arrlen <1:
            return 0
        low, hi = 0, arrlen-1
        while low<hi:
            mid = (low+hi)/2
            if target >nums[mid]:
                low=mid+1
            else:
                hi = mid
        if nums[low]<target: 
            return (low+1) 
        else: return low
