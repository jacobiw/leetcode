candidates = [8, 7, 4, 3]
target=11
def search(sumli, state, target, st):

    for i in range(st, len(candidates)):
        # state.append(i)
        if sumli + candidates[i] >= target:
            print 'fist', sumli + candidates[i]
            if sumli + candidates[i] == target:
                ans.append(state + [candidates[i]])
                print ans
            
            print state, 'and', candidates[i]
            print 'return'
            
            
            return
        
        print state
        print sumli
        raw_input()
        search(sumli+ candidates[i], state+[candidates[i]], target, i)
        # state.pop()
        

ans = []

search(0, [], target, 0)
print ans
