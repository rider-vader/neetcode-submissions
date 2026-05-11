class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        dp=[0] * len(nums)
        for i in range(len(nums)):
            if i ==0 or i ==1:
                dp[i]=nums[i]
            elif i ==2:
                dp[i]=nums[i]+dp[0]
            else:
                dp[i]= max(dp[i-2],dp[i-3]) + nums[i]
        return max(dp)