class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        s, e = 0, R * C - 1

        while s <= e:
            mid = s + (e - s) // 2
            if matrix[mid//C][mid%C] < target:
                s = mid + 1
            elif matrix[mid//C][mid%C] > target:
                e = mid - 1
            else:
                return True
        return False
        # 