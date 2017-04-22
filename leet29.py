class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        maxint= 2**31-1
        minint =-1*2**31
        if divisor == 0 or (dividend == minint and divisor == -1):
            return maxint
            
        negative=0

        if dividend<0:
            negative+=1
            dividend =abs(dividend)
        if divisor<0:
            negative+=1
            divisor = abs(divisor)
        if dividend ==0:
            return 0
        
        shift = 32
        ans=0
        count=0
        while shift >=0:
            if dividend >= divisor<<shift:
                dividend -= divisor<<shift
                count += 1<<shift
            shift -= 1
        ans = count
        if negative==1:
            ans *=-1
        if ans > maxint:
            return maxint
        if ans < minint:
            return minint
        return ans
            

            
        
