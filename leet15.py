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
# n^2
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
        newnums = nums
        arrlen= len(nums)
        
        for i in xrange(arrlen-2):
            if i and newnums[i] == newnums[i-1]:
                continue
            L,R = i+1, arrlen-1
            target = -1* newnums[i]
            # if newnums[L] == newnums[L+1]:
            #     L+=1
            # if newnums[R] == newnums[R-1]:
            #     R-=1
            while R>L:
                sumrl = newnums[L] + newnums[R]
                if sumrl == target:
                    ans.append([newnums[i],newnums[L],newnums[R]])
                    R-=1
                    L+=1
                    # if R>L:
                    while R>L and newnums[L] == newnums[L-1]:
                        L+=1
                    while R>L and newnums[R] == newnums[R+1]:
                        R-=1
                elif sumrl > target:
                    R-=1
                else:
                    L+=1
        return ans
        
 
       
        
