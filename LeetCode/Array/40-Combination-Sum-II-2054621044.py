class Solution:
    def func(self,index,n,candidates,target,ans):
        if target==0:
            ans.append(n[:])
            return
        if target<0 or index==len(candidates):
            return
        n.append(candidates[index])
        self.func(index+1,n,candidates,target-candidates[index],ans)
        n.pop()
        for i in range(index+1,len(candidates)):
            if candidates[i]!=candidates[index]:
                self.func(i,n,candidates,target,ans)
                break
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        self.func(0,[],candidates,target,ans)
        return ans