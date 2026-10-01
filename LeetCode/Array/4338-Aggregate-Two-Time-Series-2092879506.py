class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        i=len(series1)-1
        j=len(series2)-1
        v1=0
        v2=0
        ans=[]
        while i>=0 or j>=0:
            if j<0 or (i>=0 and series1[i][0]>series2[j][0]):
                v1=series1[i][1]
                ans.append([series1[i][0],v1+v2])
                i-=1
            elif i<0 or (j>=0 and series2[j][0]>series1[i][0]):
                v2=series2[j][1]
                ans.append([series2[j][0],v1+v2])
                j-=1
            else:
                v1=series1[i][1]
                v2=series2[j][1]
                ans.append([series1[i][0],v1+v2])
                i-=1
                j-=1
        ans.reverse()
        return ans
