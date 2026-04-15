# Better than swap approach:
# Swap = 3 assignments
# This = 1 assignment per element
# Time Complexity:  O(n) + O(n) = O(n)

# Space Complexity: O(1)

# ⚠️ Note:
# Two passes
# Fewer writes than swap

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        
        # Step 1: Move non-zero elements forward
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        # Step 2: Fill remaining with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0

        return nums