class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans=''
        l1, l2= len(num1), len(num2)
        if l1==0 or l2==0: return ''
        if num1=='0' or num2=='0': return '0'
        temp =  [0]*(l1+l2)

        for i in xrange(l1-1,-1,-1):
            for j in xrange(l2-1,-1,-1):
                tempsum = int(num1[i])*int(num2[j]) + temp[i+j+1]
                temp[i+j]+= tempsum/10
                temp[i+j+1]=tempsum%10
        for i in xrange(l1+l2):
            if i ==0 and temp[i]==0: 
                continue
            ans+=str(temp[i])
        return ans
            
                
            
