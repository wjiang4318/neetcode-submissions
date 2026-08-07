class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]: #if value does not equal value behind -> unique
                nums[left] = nums[right]
                left +=1
            # if value does equal meaning dupli
        return left
