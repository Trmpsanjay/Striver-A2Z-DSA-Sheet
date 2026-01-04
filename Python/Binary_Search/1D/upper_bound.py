class Solution:
    def upperBound(self, arr, target):
        """
        Upper Bound = first index where arr[idx] > target
        (insertion position to keep array sorted, after all <= target)

        Works on sorted (non-decreasing) array.

        Logic:
        - If arr[mid] <= target: upper bound must be to the right -> low = mid+1
        - Else arr[mid] > target: mid is a candidate answer -> move left to find earlier -> high = mid-1
        """

        low = 0
        high = len(arr) - 1
        ans = len(arr)  # default: not found, insert at end

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] <= target:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans
