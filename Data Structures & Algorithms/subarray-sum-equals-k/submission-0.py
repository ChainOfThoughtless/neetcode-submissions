class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix + hash
        curr_sum, prefix_cnt = 0, defaultdict(int)
        prefix_cnt[0] += 1
        res = 0
        for n in nums:
            curr_sum += n
            if curr_sum - k in prefix_cnt:
                res += prefix_cnt[curr_sum - k]
            prefix_cnt[curr_sum] = prefix_cnt.get(curr_sum, 0) + 1
        return res
