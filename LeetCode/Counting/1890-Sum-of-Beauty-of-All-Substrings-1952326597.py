class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1
                non_zero = [f for f in freq if f > 0]
                max_f = max(non_zero)
                min_f = min(non_zero)
                total_beauty += max_f - min_f
        return total_beauty


        