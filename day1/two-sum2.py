# (HashMap) → O(n)
# Instead of searching, store what you need.
# Time Complexity:O(n)
# Pattern: Hashing / Lookup optimization
def two_sum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i