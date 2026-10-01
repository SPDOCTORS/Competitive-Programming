class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        result = 0
        for i, ch in enumerate(s):
            last[ch] = i
            result += 1 + min(last['a'], last['b'], last['c'])

        return result

            
        