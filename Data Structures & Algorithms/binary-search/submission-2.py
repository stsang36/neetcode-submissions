class Solution:
    def search(self, nums: List[int], target: int) -> int:


        n = len(nums)
        left = 0
        right = n - 1

        return self.helper(nums, left, right, target)

    def helper(self, nums, left, right, target):

        if left > right:
            return -1
        
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.helper(nums, mid + 1, right, target)
        else:
            return self.helper(nums, left, right-1, target)
        
        return -1
        