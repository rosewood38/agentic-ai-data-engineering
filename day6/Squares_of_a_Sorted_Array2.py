class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        
        # Fill from largest to smallest
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        return res

# Time Complexity: O(n).You only pass through the array once.
# Space Complexity: O(n) (or o(1) if you don't count the output array), as you no longer need the extra overhead for the sorting algorithm.