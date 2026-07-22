class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best = float("-inf")

        currSum = 0
        for num in nums:
            currSum = max(num, currSum + num)
            best = max(best, currSum)
        
        return best
         

        