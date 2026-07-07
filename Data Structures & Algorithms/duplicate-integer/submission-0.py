class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = dict()

        for num in nums:
            
            if seen.get(num) is None:
                seen[num] = True
            else:
                return True
        return False


        