class Solution(object):
    def maxDepth(self, s):
        stack = []
        max_depth = 0
        for c in s:
            if c == '(':
                stack.append(c)
                max_depth = max(max_depth, len(stack))
            elif c == ')':
                if stack:
                    stack.pop()
        return max_depth
        