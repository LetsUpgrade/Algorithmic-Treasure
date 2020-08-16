class Solution:
    def findKLargest(self, nums: List[int], k: int) -> int:
         nums.sort()
         l=len(nums) 
         return nums[l-k:]