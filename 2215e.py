class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 1. Find the differences of nums1 in nums2
        # 2. Vice versa
        ans1 = set(nums1) - set(nums2)
        ans2 = set(nums2) - set(nums1)
        return [ans1, ans2]