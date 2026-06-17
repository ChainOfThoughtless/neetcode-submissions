class Solution:
    def isValid(self, s: str) -> bool:
        left_pair = set(['(', '{', '['])
        stack = []
        for c in s:
            if c in left_pair:
                stack.append(c)
            else:
                if stack and (stack[-1] == '(' and c == ')' \
                or stack[-1] == '{' and c == '}' \
                or stack[-1] == '[' and c == ']'):
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False