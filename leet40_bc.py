class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def search(sumli, state, st):
            for i in range(st, len(candidates)):
                if i>st and candidates[i-1] == candidates[i]: continue # improt check
                if sumli + candidates[i] >= target:
                    if sumli + candidates[i] == target:
                        ans.append(state+[candidates[i]])
                    return
                search(sumli + candidates[i],state+[candidates[i]],i+1 )
        ans =[]
        candidates.sort()
        search(0,[],0)
        # print ans
        return ans
