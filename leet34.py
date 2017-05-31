class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arrlen = len(nums)
        ans=[]
        low, hi = 0, arrlen-1
        fail = [-1,-1]
        if arrlen <1:
            return fail
        
        while hi >low:
            mid = (hi+low)/2
            if target > nums[mid]:
                low = mid+1
            else:
                hi = mid
        if target == nums[low]:
            ans.append(low)
        else:
            return fail
        hi = arrlen-1
        while hi > low:
            mid = (hi+low)/2 +1
            if target < nums[mid]:
                hi=mid-1
            else:
                low= mid
        ans.append(hi)
        return ans
////            
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search (hi,low, target):
            while hi >low:
                mid = (hi+low)/2
                if target > nums[mid]:
                    low = mid+1
                else:
                    hi = mid
            return low
        arrlen = len(nums)
        ans=[]
        low, hie = 0, arrlen-1
        fail = [-1,-1]
        if arrlen <1:
            return fail
        p1 = search(hie,low,target)
        if not nums[p1] == target: return fail
        p2 = search(hie,p1,target+1)
        if nums[p2] == target: return [p1,p2]
        return [p1,p2-1]
        
        
