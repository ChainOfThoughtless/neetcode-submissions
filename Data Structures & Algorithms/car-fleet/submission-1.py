class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = [] # mono increase stack 
        for p, s in pair:
            ETA = ((target - p) / s)
            if stack and stack[-1] >= ETA:
                continue
            stack.append(ETA)
        return len(stack)

