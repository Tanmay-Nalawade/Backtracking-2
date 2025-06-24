# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:

#         # ZERO ONE RECURSION SOLUTION

#         self.result = []
#         self.helper(nums, 0, [])
#         return self.result
#     def helper(self, nums, idx, path):
#         # Base
#         if idx == len(nums):
#             self.result.append(list(path))
#             return

#         # action

#         # not choose
#         self.helper(nums, idx + 1, path)
#         # choose 
#         path.append(nums[idx])
#         self.helper(nums, idx + 1, path)
#         path.pop()



# FOR LOOP BASED RECURSION

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper(nums, 0, [])
        return self.result
    def helper(self, nums, pivot, path):
        # No need for base case because we have to append to results at every node
        self.result.append(list(path))
        
        for i in range(pivot , len(nums)):
            # action
            path.append(nums[i])
            # recurse
            self.helper(nums, i + 1, path)
            # backtrack
            path.pop()