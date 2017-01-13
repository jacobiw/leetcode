//list solution
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlen = len(s)
        idx=0
        out=0
        sidx=0
        romanlist=['I','V','X','L','C','D','M']
        intlist =[1,5,10,50,100,500,1000]
        if s=='':
            return 0
        while strlen-sidx-1 >=0:
            if s[strlen-sidx-1]==romanlist[idx]:
                out+=intlist[idx]
                sidx+=1
            else:
                idx+=1
            if idx>0 and strlen-sidx-1 >=0 and s[strlen-sidx-1] in romanlist[0:idx-1]:
                for iidx in xrange(idx-1):
                    if s[strlen-sidx-1]==romanlist[iidx]:
                        # sidx+=1
                        out-=intlist[iidx]
                        sidx+=1
            
        return out
            
        
            
