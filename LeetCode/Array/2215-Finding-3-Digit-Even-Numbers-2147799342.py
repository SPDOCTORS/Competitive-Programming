class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        res=[]
        freq=Counter(digits)
        for i in range(100,1000,2):
            freq1=Counter(int(d) for d in str(i))
            if all(freq[d]>=freq1[d] for d in freq1):
                res.append(i)
        return res        