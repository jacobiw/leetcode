class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        arraylen = len(nums)
        ans =[]
        if len ==0:
            return []
        for i in xrange(arraylen-3):
            if i and nums[i-1]==nums[i]:
                continue
            for j in xrange(i+1,arraylen-2):
                if nums[j-1] == nums[j] and j != i+1:
                    continue
                L,R = j+1,arraylen-1
                sums = target - nums[i]-nums[j]
                while R>L:
                    sumRL = nums[R]+nums[L]
                    if  sumRL == sums:
                        # keep answers and keep search
                        ans.append([nums[i],nums[j],nums[L],nums[R]])
                        L+=1
                        R-=1
                        while R>L and nums[L]==nums[L-1]:
                            L+=1
                        while R>L and nums[R]==nums[R+1]:
                            R-=1
                    elif sumRL-sums >0:
                        R-=1
                    else:
                        L+=1
        return ans
        
