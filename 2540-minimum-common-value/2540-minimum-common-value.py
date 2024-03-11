class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        l = list(set(nums1) & set(nums2))
        return -1 if not l else min(l)