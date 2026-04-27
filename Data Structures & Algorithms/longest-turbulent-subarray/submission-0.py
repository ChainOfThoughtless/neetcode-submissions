class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #sliding window
        l, r = 0, 1
        res, sign = 1, ""
        while r < len(arr):
            if arr[r - 1] < arr[r] and sign != "<":
                res = max(res, r - l + 1)
                r += 1
                sign = "<"
            elif arr[r - 1] > arr[r] and sign != ">":
                res = max(res, r - l + 1)
                r += 1
                sign = ">"
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                sign = ""
        return res