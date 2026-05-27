from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq map
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        # min heap: freq, num
        min_heap = []
        for num, freq in freq_map.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)

        return [num for freq, num in min_heap]