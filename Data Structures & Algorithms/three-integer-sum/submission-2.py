class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        nums.sort()
        res = list()

        for i in range(n-2):

            if nums[i] == nums[i-1] and i > 0:
                continue;
            
            left = i+1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right] 

                if s < 0:
                    left +=1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    
        return res
