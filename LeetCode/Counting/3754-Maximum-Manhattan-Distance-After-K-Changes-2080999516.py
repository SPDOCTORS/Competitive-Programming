class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        north=0
        south=0
        east=0
        west=0
        maxi=0
        for i,ch in enumerate(s):
            if ch=='N':
                north+=1
            elif ch=='S':
                south+=1
            elif ch=='E':
                east+=1
            elif ch=='W':
                west+=1
            x=abs(east-west)
            y=abs(north-south)
            MD=x+y
            steps=i+1
            wastedstep=steps-MD
            extrastep=min(2*k,wastedstep)
            finalMD=MD+extrastep
            maxi=max(maxi,finalMD)
        return maxi