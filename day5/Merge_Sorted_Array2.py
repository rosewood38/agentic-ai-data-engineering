# Micro-optimized single-pass version (clean interview version)
class Solution:
    def merge(nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:   # ONLY j controls termination
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# We remove second cleanup loop entirely
# We ensure nums2 is fully consumed
# nums1 leftover automatically stays in place
# One-line intuition

# We loop until nums2 is empty because nums2 is the only array that may still need copying.
# Time Complexity: O(m + n)
# Space: O(1) (in-place)