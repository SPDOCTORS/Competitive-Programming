class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        current=0
        ans=0
        n=len(requests)
        for i in range(n):
            time=abs(requests[i]-current)
            current=requests[i]
            ans+=time
        return ans
        