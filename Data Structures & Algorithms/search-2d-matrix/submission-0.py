class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        n = len(matrix)

        low_row_idx = 0
        high_row_idx = n - 1


        

        while (high_row_idx >= low_row_idx):
            mid = low_row_idx + (high_row_idx - low_row_idx) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid]
                n_row = len(row)
                l = 0
                r = n_row - 1

                while l <= r:
                    mid_r = l + (r - l) // 2

                    if row[mid_r] == target:
                        return True
                    elif row[mid_r] < target:
                        l = mid_r + 1
                    else:
                        r = mid_r - 1
            
                return False

            if matrix[mid][-1] < target:
                low_row_idx = mid + 1
            else:
                high_row_idx = mid - 1

        return False 

        