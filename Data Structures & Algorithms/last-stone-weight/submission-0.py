class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[-1]
        mh = [-s for s in stones]
        heapq.heapify(mh)
        print("-stone", mh)
        while len(mh) > 2:
            x = heapq.heappop(mh)
            y = heapq.heappop(mh)
            if x < y:
                heapq.heappush(mh, x - y) 
            print('loop:', mh)   
        if len(mh) == 2:
            print('final:', mh)
            return -(mh[0] - mh[1])
        return -mh[-1]
            
