class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        l=nums[-1*k:]
        nums[k:]=nums[:-k]
        nums[:k]=l
