class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        rest ={}
        for index in xrange(len(nums)):
            another = target - nums[index]
            if nums[index] in rest:
                return [rest[nums[index]], index]
            else:
                rest[another]=index
        return []
                    
