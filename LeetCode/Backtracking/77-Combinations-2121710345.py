class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        subsets=[]
        def backtrack(start):
            if len(subsets)==k:
                ans.append(subsets[:])
                return 
            for num in range(start, n + 1):
                subsets.append(num)
                backtrack(num + 1)
                subsets.pop()

        backtrack(1)
        return ans



        