class Solution:
    def func(self,candidates,index,target,path,ans):
        if target==0:
            ans.append(path[:])
            return
        if target<0 or index==len(candidates):
            return
        path.append(candidates[index])
        self.func(candidates,index,target-candidates[index],path,ans)
        path.pop()
        self.func(candidates,index+1,target,path,ans)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        self.func(candidates,0,target,[],ans)
        return ans
        