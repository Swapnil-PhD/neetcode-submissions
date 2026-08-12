class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] > target or matrix[m-1][n-1] < target:
            return False
        
        lr,rr = 0, m-1
        while lr <= rr:
            mid_r = (lr+rr)//2
            if matrix[mid_r][0]<=target and matrix[mid_r][n-1]>= target:
                lc,rc = 0, n-1
                while lc <= rc:
                    mid_c = (lc+rc)//2
                    if matrix[mid_r][mid_c] == target:
                        return True
                    elif matrix[mid_r][mid_c] > target:
                        rc = mid_c - 1 
                    else:
                        lc = mid_c + 1
                    
                return False
            elif matrix[mid_r][0]<=target and matrix[mid_r][n-1]<= target:
                lr = mid_r +1
            else:
                rr = mid_r -1
        return False

        
        