class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1,m1,s1=map(int,startTime.split(":"))
        h2,m2,s2=map(int,endTime.split(":"))
        sec1=h1*3600+m1*60+s1
        sec2=h2*3600+m2*60+s2
        return sec2-sec1

        