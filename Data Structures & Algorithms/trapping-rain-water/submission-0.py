class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n
        for i in range(0,n-1):
            right_max[i] = max(height[i+1:])
            
        for i in range(1,n):
            left_max[i] = max(height[:i])
        
        area = 0
        for i in range(n):
            pot = min(left_max[i],right_max[i])
            area += max( pot - height[i],0)
        
        return area
        