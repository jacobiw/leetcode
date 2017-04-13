class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        dic['(']=')'
        dic['[']=']'
        dic['{']='}'
        arr=[]
        idx=0
        if len(s)<2:
            return False
        for i in s:
            if i in dic.keys():
                arr.append(i)
                idx+=1
            else:
                if idx==0:
                    return False
                temp = arr.pop()
                if i == dic[temp]:
                    idx-=1
                else:
                    return False
        if idx ==0:
            return True
        else:
            return False
                
        # False: i<0, (}, ()), (((()
            
        
