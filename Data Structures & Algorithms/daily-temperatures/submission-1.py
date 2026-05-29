class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (t, index)
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((t, i))
        return res