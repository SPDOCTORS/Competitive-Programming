class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        self.generate(0,0,n,"",ans)
        return ans


    def generate(self,opencount,closecount,n,current,ans):
        if opencount==closecount==n:
            ans.append(current)
        if opencount<n:
            self.generate(opencount+1,closecount,n,current+"(",ans)
        if closecount<opencount:
            self.generate(opencount,closecount+1,n,current+")",ans)
        
        