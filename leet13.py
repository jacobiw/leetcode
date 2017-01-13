# //list solution
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
# hash type
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtoi={}
        
        
        strlen = len(s)
        realen=len(s)
        idx=0
        out=0
        sidx=0
        romanlist=['I','V','X','L','C','D','M']
        intlist =[1,5,10,50,100,500,1000]
        strlen-=1
        for ii in xrange(len(intlist)):
            rtoi[romanlist[ii]]=intlist[ii]
        if s=='':
            return 0
        while strlen>=0:
        # for sidx in xrange(strlen):
            out+=rtoi[s[strlen]]
            # if strlen-1>0 and strlen+1<realen-1:
            if strlen-1>=0:
                if rtoi[s[strlen-1]]<rtoi[s[strlen]]:
                    out-=rtoi[s[strlen-1]]
                    strlen-=1
            strlen-=1
            
            
        return out
            
        
            
        
            
