# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._helper(pairs, 0, len(pairs) - 1)
    
    def _helper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        m = (s + e) // 2
        self._helper(pairs, s, m)
        self._helper(pairs, m + 1, e)
        self.merge(pairs, s, m, e)
        return pairs

    def merge(self, arr, s, m, e):
        left = arr[s: m + 1]
        right = arr[m + 1: e + 1]
        i, j, idx = 0, 0, s
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[idx] = left[i]
                i += 1
            else:
                arr[idx] = right[j]
                j += 1
            idx += 1
        while i < len(left):
            arr[idx] = left[i]
            i += 1
            idx += 1
        while j < len(right):
            arr[idx] = right[j]
            j += 1
            idx += 1
