class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        t = "1" + s + "1"

        n = len(t)
        i = 0

        prev = None
        curr = None
        maxGain = 0

        while i < n:
            ch = t[i]
            j = i
            while j < n and t[j] == ch:
                j += 1

            nxt = (ch, j - i)

            if prev and curr:
                if prev[0] == '0' and curr[0] == '1' and nxt[0] == '0':
                    maxGain = max(maxGain, prev[1] + nxt[1])

            prev = curr
            curr = nxt
            i = j

        return ones + maxGain