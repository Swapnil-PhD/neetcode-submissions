class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        n = len(height)

        left_max = [0]*n
        right_max = [0]*n
        for i in range(n):
            left_max[i] = l
            l = max(height[i],l)
        for i in range(n-1,-1,-1):
            right_max[i] = r
            r = max(height[i],r)

        max_area = 0
        for i in range(n):
            max_area += max((min(left_max[i],right_max[i])-height[i]),0)

        return max_area


        