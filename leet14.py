class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs)<=1:
            return strs[0] if len(strs)==1 else ""
            
        shortstr = min(len(s) for s in strs)
        if shortstr ==0:
            return ''
        ans=''
        idx=0
        
        while idx <shortstr:
            pif = strs[0][idx]
            for sidx in xrange(len(strs)):
                
                
                if not strs[sidx][idx] == pif:
                    return ans
            ans += pif
            idx+=1
        return ans
down-counting is not avaliable for this question 
        
