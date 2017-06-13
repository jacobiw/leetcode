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
#         ^ this code will change start condition for for loop, it can avoid [2,2,3]/ [2,3,2], and [2,2,2,2],[2,2,2,3].....
        candidates = [2, 3, 6, 7]
        target=7
        def search(sumli, state, target, ans):
            if sumli >= target:
                if sumli == target:
                    ans.append(state)
                    print ans
                print 'return'
                return
            for i in candidates:
                # state.append(i)
                print state
                print sumli
                raw_input()
                search(sumli+i, state+[i], target, ans)
                # state.pop() 
        ans = []
        search(0, [], target, ans)
        print ans
        
#         ^ this code is the simplist dfs        
        candidates = [2, 3, 6, 7]
        target=7
        def search(sumli, state, target, st):
            if sumli >= target:
                if sumli == target:
                    ans.append(state)
                    # print ans
                return
            for i in range(st, len(candidates)):
                # state.append(i)
                print state
                print sumli
                raw_input()
                search(sumli+ candidates[i], state+[candidates[i]], target, i)
                # state.pop()
        ans = []
        search(0, [], target, 0)
        print ans
 #         ^ this code will change start condition for for loop, it can avoid [2,2,3]/ [2,3,2]       
