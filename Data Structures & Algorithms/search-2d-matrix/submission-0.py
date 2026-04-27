class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        return self.bs(matrix, target, 0, r * c)

    def bs(self, matrix, target, s, e):
        if s > e:
            return False
        mid = s + (e - s) // 2
        r, c = self.index2coord(matrix, mid)
        print("mid", mid, "r:", r, " c:", c)
        if r >= 0 and c >= 0:
            if matrix[r][c] > target:
                e = mid - 1
            elif matrix[r][c] < target:
                s = mid + 1
            else:
                return True
            return self.bs(matrix, target, s, e)
        else:
            return False
    
    def index2coord(self, matrix, idx):
        if len(matrix) <= 0 or idx < 0:
            return -1, -1
        r, c = len(matrix), len(matrix[0])
        ans_r, ans_c = idx // c , idx % c
        print("ans_r", ans_r, "ans_c", ans_c)
        if 0 <= ans_r < r and 0 <= ans_c < c:
            return ans_r, ans_c
        return -1, -1