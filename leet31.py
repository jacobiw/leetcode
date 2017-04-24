class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything modify nums in-place instead.
        """
        arrlen = len(nums)
        check = 0
        
        if arrlen ==1 or arrlen ==0:
            return
        for idxR in xrange(arrlen-1,-1,-1):
            idxL = idxR-1
            if idxR and nums[idxL] < nums[idxR]:
                # nums[idxL],nums[idxR] = nums[idxR],nums[idxL]
                check=idxR
                break
        if check == 0:
            nums.reverse()
            return 
        # reverse
        target = idxL
        tail=arrlen-1
        while tail>check: 
            nums[check],nums[tail] = nums[tail] , nums[check]
            check+=1
            tail-=1
        for i in xrange(idxR,arrlen):
            if nums[i] > nums[idxL]:
                nums[i], nums[idxL] = nums[idxL], nums[i]
                break

                
            
        
