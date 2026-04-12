# Better (Sorting + Two Pointers) → O(n log n)
# We will use:
# Sort array
# Use left & right pointers
# Problem: We lose original indices → need extra work

def two_sum(nums, target):
    arr = [(num, i) for i, num in enumerate(nums)]
    arr.sort()

    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left][0] + arr[right][0]

        if s == target:
            return [arr[left][1], arr[right][1]]
        elif s < target:
            left += 1
        else:
            right -= 1