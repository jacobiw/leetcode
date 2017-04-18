class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # totalW = len(height)
        p1,p2 = 0, len(height)-1
        # curV = min(height(p1),height(p2))*(p1-p2)
        maxV=min(height[p1],height[p2])*(p2-p1)
        ansidx=[p1,p2]
        while p2>p1:
            # i need to scan every case of each side

            if height[p1] >= height[p2]:
                p2-=1
                # while p2>p1 and height[p1] >= height[p2]:
                #     p2-=1
            else:
                p1+=1
                # while p2>p1 and height[p1] <= height[p2]:
                #     p1+=1

            curV = min(height[p1],height[p2])*(p2-p1)
            if curV>maxV:
                ansidx=[p1,p2]
                maxV=curV
            if p2==p1+1:
                break
        return maxV
            
        
