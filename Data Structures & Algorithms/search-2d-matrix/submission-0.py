class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2
            current_value = matrix[mid // cols][mid % cols]
            if current_value == target:
                return True
            elif current_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False