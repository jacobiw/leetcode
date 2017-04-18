class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        state=''
        ans=[]
        maxlayer=n
        def bt(layer, state, maxlayer,left,right):
            if layer == maxlayer*2:
                ans.append(state)
                return
            if left < maxlayer:
                bt(layer+1,state+'(',maxlayer,left+1,right)
                
            if right< left:
                bt(layer+1,state+')',maxlayer,left,right+1)
                
        bt(0,'',n,0,0)
        return ans
            
                
        
