# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qs_helper(pairs, 0, len(pairs) - 1)
        return pairs
        
    def qs_helper(self, arr, s, e):
        if e - s + 1 <= 1:
            return
        pivot = arr[e]
        left = s
        for i in range(s, e):
            if arr[i].key < pivot.key: #1 sift right
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        #2 swap pivot to middle
        arr[left], arr[e] = arr[e], arr[left]

        #3 recursively qs
        self.qs_helper(arr, s, left - 1)
        self.qs_helper(arr, left + 1, e)