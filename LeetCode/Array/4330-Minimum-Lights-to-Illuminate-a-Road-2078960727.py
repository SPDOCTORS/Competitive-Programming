class Solution:
    def minLights(self, lights: list[int]) -> int:
        n=len(lights)
        diff=[0]*(n+1)
        for i,v in enumerate(lights):
            if v>0:
                left=max(0,i-v)
                right=min(n-1,i+v)
                diff[left]+=1
                if right+1<n:
                    diff[right+1]=-1
        visited=[False]*n
        curr=0
        for i in range(n):
            curr+=diff[i]
            if curr>0:
                visited[i]=True
        ans=0
        i=0
        while i<n:
            if visited[i]:
                i+=1
            else:
                start=i
                while i<n and not visited[i]:
                    i+=1
                length=i-start
                ans+=(length+2)//3
        return ans
        