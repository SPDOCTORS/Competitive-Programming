class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        max_lights=max(lights)
        maxi=0
        for arrival in arrivalTime:
            r=arrival%period
            if r<max_lights:
                wait=0
            else:
                wait=period-r
            if wait>maxi:
                maxi=wait
        return maxi
        