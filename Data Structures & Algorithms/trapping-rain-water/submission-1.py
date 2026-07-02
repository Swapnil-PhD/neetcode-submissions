class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = 0 
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n

        for i in range(n):
            j = -i-1
            max_left[i] = l
            max_right[j] = r
            l = max(l, height[i])
            r = max(r, height[j])

        trap = 0
        for i in range(n):
            potential = min(max_left[i],max_right[i])
            trap += max(0, (potential-height[i]))

        return trap
