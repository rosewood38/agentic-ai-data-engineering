# Squares of a Sorted Array
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#  Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#  Time Complexity: O(nlogn)
#  Space Complexity: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr1=[i*i for i in nums]
        arr1.sort()
        return arr1