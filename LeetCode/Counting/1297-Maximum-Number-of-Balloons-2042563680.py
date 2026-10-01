from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=Counter(text)
        required={'b':1,'a':1,'l':2,'o':2,'n':1}
        return min(count[ch]//required[ch] for ch in required)



        