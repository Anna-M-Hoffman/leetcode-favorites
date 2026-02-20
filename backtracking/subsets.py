# SUBSETS

# Given an array nums of unique integers,
#  return all possible subsets of nums.

# The solution set must not contain duplicate subsets. 
# You may return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # All possible subsets - order does not matter = POWER SET
        # An empty subset is a subset
        # 2^n subsets are possible
        res = []
        subset = [] 

        def dfs(i):
            if i >= len(nums): # i is out of bounds = just return
                res.append(subset.copy())
                # The subset will be modified going forward, copy takes a snapshot
                return 

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Do not include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
        
