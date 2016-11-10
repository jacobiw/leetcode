class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums=[]
        ans=''
        # for num in xrange(10):
        #     nums.append(str(num))
        nums = ['0','1','2','3','4','5','6','7','8','9']
        signs = ['-','+']
        total = nums+signs
        sign1=0
        sign2=0
        if (len(str)==0):
            return 0
        news = str.split()
        if news[0][0] not in total:
            return 0
        for ele in news[0]:
            if ele not in total:
                break
            else:
                if ele == '+':
                    sign1 += 1
                elif ele == '-':
                    sign2 += 1
                elif sign1 >1 or sign2 >1 or (sign1 ==1 and sign2 ==1):
                    return 0
                if ele in nums:
                    ans+=ele
        if len(ans)==0:
            return 0
        realans = int(ans)
        if sign2==1:
            realans*=-1
        if realans < -(1<<31):
            realans=-(1<<31)
        elif realans> (1<<31)-1:
            realans=(1<<31)-1
        return realans

        
