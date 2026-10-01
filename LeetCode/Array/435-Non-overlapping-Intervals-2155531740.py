class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        limit=intervals[0][1]
        cnt=1
        n=len(intervals)
        for i in range(1,n):
            if intervals[i][0]>=limit:
                limit=intervals[i][1]
                cnt+=1
        return n-cnt
        