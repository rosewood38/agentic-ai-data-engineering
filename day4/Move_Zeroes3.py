# Single-Pass + Minimal Writes (Best Version)
# Only write when needed
# Avoid unnecessary swaps
# Avoid rewriting same value

# Time Complexity: O(n) (single pass)

# Space Complexity: O(1)

#  Best properties:

# Single pass
# Minimum writes
# No unnecessary swaps

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insertpos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                # Only write when positions differ
                if i != insertpos:
                    nums[insertpos] = nums[i]
                    nums[i] = 0
                insertpos += 1