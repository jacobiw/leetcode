class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {}
        phone['2']=['a','b','c']
        phone['3']=['d','e','f']
        phone['4']=['g','h','i']
        phone['5']=['j','k','l']
        phone['6']=['m','n','o']
        phone['7']=['p','q','r','s']
        phone['8']=['t','u','v']
        phone['9']=['w','x','y','z']
        
        ans=[]
        deepth = len(digits)
        
        if digits =='':
            return []
        
        def dfs(deep,state,ans):
            if deep == deepth:
                ans.append(state)
                return 
            for letters in phone[digits[deep]]:
                dfs(deep+1,state+letters,ans)
            
        dfs(0,'',ans)
        return ans
            
        
        
        
        
