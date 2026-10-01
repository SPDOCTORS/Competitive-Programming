class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        startpar=(start[0]+start[1])%2
        targetpar=(target[0]+target[1])%2
        if startpar==targetpar:
            return True
        else:
            return False
        