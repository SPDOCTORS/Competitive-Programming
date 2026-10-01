class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(left,right):
            if left==right:
                return nums[left]
            leftie=nums[left]-winner(left+1,right)
            rightie=nums[right]-winner(left,right-1)
            return max(leftie,rightie)
        return winner(0,len(nums)-1)>=0
            

            

        