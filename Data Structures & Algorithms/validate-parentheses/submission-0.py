class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in pair.values():
                stack.append(c)
            else:
                #found closing
                if len(stack) < 1 or pair[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0