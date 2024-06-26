class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        
        nums = set(nums)
        
        for num in nums:
            if num - 1 not in nums:
                seq = 1
                while num + seq in nums:
                    seq += 1
                
                longest = max(longest, seq)
        
        return longest