class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        far=0
        for i in range(len(nums)):
            if i>far:
                return False
            far=max(far,i+nums[i])
        return True