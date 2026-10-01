class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = 0

        for c in s:
            if c == "*":
                n = max(n - 1, 0)
            elif c == "#":
                n <<= 1
            elif c== "%":
                continue
            else:
                n += 1

        if k >= n:
            return "."

        for c in reversed(s):
            if c == "*":
                n += 1
            elif c == "#":
                n >>= 1
                if k >= n:
                    k -= n
            elif c == "%":
                k = n - 1 - k
            else:
                n -= 1
                if n == k:
                    return c

        