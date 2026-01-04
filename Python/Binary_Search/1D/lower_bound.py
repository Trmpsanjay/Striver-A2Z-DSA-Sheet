class Solution:
    def lowerBound(self, arr, target):
        """
        Lower Bound (first index where arr[idx] >= target)

        Meaning:
        - Returns the smallest index `idx` such that arr[idx] >= target.
        - If target is bigger than all elements, returns len(arr).

        Intuition (binary search):
        - Whenever arr[mid] >= target, mid is a *possible answer*,
          but we still search left to find an earlier one.
        - Otherwise, search right.

        Works only if `arr` is sorted (non-decreasing).

        Time:  O(log n)
        Space: O(1)
        """

        low = 0
        high = len(arr) - 1
        ans = len(arr)  # default: "not found in array", insertion position at end

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                ans = mid          # mid could be the first valid position
                high = mid - 1     # try to find an even smaller index on the left
            else:
                low = mid + 1      # need larger values, go right

        return ans
