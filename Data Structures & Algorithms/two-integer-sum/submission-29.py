class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution = []
        # for i in range(len(nums)): # 0, 1, 2, 3
        #     for j in range(i+1, len(nums)): # 1, 2, 3
        #         if nums[i] + nums[j] == target:
        #             solution.extend([i,j])
        #             return solution

      hashmap = {}
      for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hashmap:
          return [hashmap[difference], i]
        hashmap[nums[i]] = i












        # hashmap = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in hashmap:
        #         return [hashmap[diff], i]
        #     hashmap[nums[i]] = i

        '''The logic:
For each number, calculate what you need to find: diff = target - current_number

Check: "Have I seen this diff before?" (in the hashmap)

i=0, nums[0]=3:
  Need: 7-3=4
  4 in hashmap? NO
  Add: {3: 0} <- store this so that if we find a complement later, we know where it is

i=1, nums[1]=4:
  Need: 7-4=3
  3 in hashmap? YES (at index 0)
  Print: [0, 1]  ✅ Found it!
  '''