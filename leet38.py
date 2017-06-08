class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def countfc(li):
            count=0
            cur=li[0]
            out=''
            for i in xrange(len(li)):
                if cur != li[i]:
                    out+=(str(count)+cur)
                    count=1
                    cur=li[i]
                else:
                    count+=1
            out+=(str(count)+cur) 
            return out
            
        
        if n ==0:
            return ''
        if n ==1:
            return '1'
        temp='1'
        for i in xrange(1,n):
            temp = countfc(temp)
        return temp
