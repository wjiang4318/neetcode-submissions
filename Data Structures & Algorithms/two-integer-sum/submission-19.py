class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i in range(len(nums)): # 0, 1, 2, 3
            for j in range(i+1, len(nums)): # 1, 2, 3
                if nums[i] + nums[j] == target:
                    solution.extend([i,j])
                    return solution
