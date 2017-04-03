class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        arrlen= len(nums)
        
        closest=abs((nums[0]+nums[1]+nums[arrlen-1])-target)
        ans = nums[0]+nums[1]+nums[arrlen-1]
        
        for i in xrange(arrlen-2):
            L,R = i+1, arrlen-1
            while R>L:
                diff = (nums[i]+nums[R]+nums[L])-target
                if abs(diff)<closest:
                    closest = abs(diff)
                    ans = nums[i]+nums[R]+nums[L]
                    # while R>L and nums[L]==nums[L-1]:
                    #     L+=1
                    # while R>L and nums[R]==nums[R+1]:
                    #     R-=1
                    if diff ==0:
                        return ans
                lissum = nums[i]+nums[R]+nums[L]
                if lissum >target:
                    R-=1
                else:
                    L+=1
        return ans
        
