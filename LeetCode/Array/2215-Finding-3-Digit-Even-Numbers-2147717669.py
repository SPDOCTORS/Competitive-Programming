class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        n=len(digits)
        seen=set()
        for i in range(n):
            if digits[i]==0:
                continue
            for j in range(n):
                if j==i:
                    continue
                for k in range(n):
                        if k==i or k==j or digits[k]%2!=0:
                            continue
                        d=digits[i]*100+digits[j]*10+digits[k]
                        seen.add(d)
        return sorted(list(seen))
        