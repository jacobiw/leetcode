class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        
        def search(sumli, state, target, st):

            for i in range(st, len(candidates)):
                if sumli+ candidates[i] >= target:
                    if sumli+ candidates[i] == target:
                        ans.append(state+[candidates[i]])
                    return
                
                search(sumli+ candidates[i], state+[candidates[i]], target, i)
                # state.pop()
                
        
        ans = []
        
        search(0, [], target, 0)
        return ans
        
        
        
