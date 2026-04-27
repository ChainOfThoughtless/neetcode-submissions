class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, SUM, res = 0, 0, 0
        for R in range(len(arr)):
            if R - L + 1 < k:
                SUM += arr[R]
                continue
            elif R - L + 1 > k:
                SUM -= arr[L]
                L += 1
            SUM += arr[R]
            avg = SUM / k
            if avg >= threshold:
                res += 1
        return res
            