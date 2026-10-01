class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:[x[0],-x[1]])
        cnt=0 
        maxiend=0
        for start,end in intervals:
            if end>maxiend:
                cnt+=1
                maxiend=end
        return cnt
        