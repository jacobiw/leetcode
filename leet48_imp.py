class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lenli= len(nums)
        # nums.sort()
        ans=[]

        def search(state,deepth,nums):
            if deepth ==lenli:
                ans.append(state)
                return
            for i in xrange(len(nums)):
                # if i> st and nums[i] == nums[i-1]:
                #     continue
                search(state+[nums[i]],deepth+1,nums[:i]+nums[i+1:])
        search([],0,nums)
        return ans
