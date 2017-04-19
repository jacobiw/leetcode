class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        stackl = len(haystack)
        needlel = len(needle)
        
        if stackl == 0:
            if needlel==0:
                return 0
            else:
                return -1
        if needlel > stackl:
            return -1
            
        curidx=0    
        for idx in xrange(stackl-needlel+1):
            if needlel==0:
                return 0
            curidx=0
            while curidx < needlel:
                
                if haystack[idx+curidx] == needle[curidx]:
                    curidx+=1
                if curidx == needlel:
                    return idx
                if haystack[idx+curidx] != needle[curidx]:
                    break
        return -1
        
