class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def search(state,deepth,nums,st):
            if deepth==maxd:
                ans.append(state)
                return
            for i in xrange(len(nums)):
                if i >0 and nums[i-1]==nums[i]: 
                    continue
                search(state+[nums[i]],deepth+1,nums[:i]+nums[i+1:],i)
        maxd= len(nums)
        ans=[]
        nums.sort()
        search([],0,nums,0)
        return ans
        
