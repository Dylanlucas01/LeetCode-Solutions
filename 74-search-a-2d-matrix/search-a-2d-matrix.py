class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        width = len(matrix[0]) -1
        target_row = None

        while top <= bottom:
            middle = (top + bottom) // 2

            if target >= matrix[middle][0] and target <= matrix[middle][width]:
                if matrix[middle][0] == target or matrix[middle][width] == target:
                    return True

                target_row = middle
                break

            if matrix[middle][0] > target:
                bottom = middle - 1

            else:
                top = middle + 1
        
        if target_row == None:
            return False

        left = 0
        right = width

        while left <= right:
            middle = (left + right) // 2

            if matrix[target_row][middle] == target:
                return True

            if matrix[target_row][middle] > target:
                right = middle - 1

            if matrix[target_row][middle] < target:
                left = middle + 1

        return False
        