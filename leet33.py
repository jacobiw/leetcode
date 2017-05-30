class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arrlen = len(nums)
        low, hi = 0, arrlen-1
        if arrlen <=1:
            if arrlen ==1 and target == nums[0]:
                return 0
            return -1
        while hi >low:
            mid = (hi+low)/2
            if (nums[0]> target) ^ (nums[0]>nums[mid]) ^ (target > nums[mid]):
                low = mid+1
            else:
                hi = mid
        return low if target in nums[low:low+1] else -1
#     //////////////////////////////////////////////////////////////////////////////
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arrlen = len(nums)
        low, hi = 0, arrlen-1
        if arrlen <=1:
            if arrlen ==1 and target == nums[0]:
                return 0
            return -1
        while hi >low:
            
            mid = (hi+low)/2
            if target == nums[mid]: return mid
            if (nums[0]> target) ^ (nums[0]>nums[mid]) ^ (target > nums[mid]):
                low = mid+1
            else:
                hi = mid
        return low if target == nums[low] else -1

                
                
                
                
                
