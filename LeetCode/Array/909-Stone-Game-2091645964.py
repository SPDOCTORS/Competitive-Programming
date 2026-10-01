from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def winner(left,right):
            if left==right:
                return piles[left]
            leftie=piles[left]-winner(left+1,right)
            rightie=piles[right]-winner(left,right-1)
            return max(leftie,rightie)
        return winner(0,len(piles)-1)>=0
            
            
        