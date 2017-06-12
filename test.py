candidates = [2, 3, 6, 7]
target=7
def search(sumli, state, target, st):
    if sumli >= target:
        if sumli == target:
            ans.append(state)
            # print ans
        
        print 'return'
        
        
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
