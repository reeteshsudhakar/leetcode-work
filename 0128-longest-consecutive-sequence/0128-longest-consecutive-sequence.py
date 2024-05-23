class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        
        nums = set(nums)
        
        for num in nums:
            if num - 1 not in nums:
                count = 1
                while num + count in nums:
                    count += 1
                longest = max(count, longest)
                
        return longest