class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        target = (m + n) // 2
        l, r = 0, m-1
        while True:
            i = (l + r) // 2
            j = target - i - 2
            nums1left = nums1[i] if i >= 0 else float("-infinity")
            nums1right = nums1[i+1] if i+1 < m else float("infinity")
            nums2left = nums2[j] if j >= 0 else float("-infinity")
            nums2right = nums2[j+1] if j+1 < n else float("infinity")

            if nums1left <= nums2right and nums2left < nums1right:
                if (m+n) % 2 == 1:
                    return min(nums1right, nums2right)
                else:
                    return (max(nums1left,nums2left)+min(nums1right,nums2right))/2.0
            elif nums1left > nums2right:
                r = i -1
            else:
                l = i + 1   
             











            

        