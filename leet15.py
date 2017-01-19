# 2sum + binary search
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        new = sorted(nums)
        tot = len(new)
        arrlen= len(new)
        m=0
        
        for i in xrange(arrlen-2):
            for j in xrange(i+1,arrlen-1):
        
                target = -(new[i]+new[j])
                L= j+1
                R=arrlen-1
                
                while not L>R:
        
                    m = (L+R)/2
                    
                    if (new[m]<target):
                        L=m+1
                    elif (new[m]>target):
                        R=m-1
                    else:
                        newans = [new[i],new[j],new[m]]
                        if newans not in ans:
                            ans.append(newans)
                        break
        return ans
        
