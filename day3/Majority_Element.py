# 169. Majority Element
# Easy
# Topics
# premium lock icon
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        count =1
        for i in nums:
             hashmap[i] = hashmap.get(i, 0) + 1
        # arr=[]
        print(hashmap)
        for i,k in hashmap.items():
            if hashmap[i]>len(nums)//2:
                return i
# Time: O(n)
# Space: O(n)