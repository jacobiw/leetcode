class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        cluster =0
        ans=[[]]
        for i in strs:
            ele = ''.join(sorted(i))
            if ele not in dic.keys():
                dic[ele] = cluster
                if cluster: ans.append([])
                cluster+=1
            ans[dic[ele]].append(i)
        return ans
# ^^^^time limit exceed 
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        cluster =0
        ans=[]
        dict = {}
        for i in strs:
            ele = ''.join(sorted(i))
            dic[ele] = [i] if ele not in dic else dic[ele]+[i]
            # if ele not in dic.keys():
            #     dic[ele] = [i]
            # else:
            #     dic[ele]+=[i]
        for key in dic:
            ans+=[dic[key]]
        return ans


                

                
                
