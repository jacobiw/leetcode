class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        idx=0
        ans=[]
        maxc = len(nums)
        while idx < maxc:

            
            while idx < maxc and nums[idx-1]==nums[idx] and idx:
                idx+=1
            if idx == maxc:
                break
            nums[count] = nums[idx] 
            count+=1
            
            idx+=1
                

        return count
        
