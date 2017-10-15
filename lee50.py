class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0: return 1
        if n<0:
            x=1/x
            n*=-1
        # return n%2==0 ? myPow(x*x, n/2) : x*myPow(x*x, n/2);
        return self.myPow(x*x, n/2) if n%2==0 else x*self.myPow(x*x, n/2)
    
        
