from typing import List

class Solution:
    def lowerBound(self, arr: List[int], target: int) -> int:
        """
        Return the first index `idx` such that arr[idx] >= target.
        If no such index exists, return len(arr).

        This is the classic "lower bound" / insertion position on the LEFT.
        """
        low, high = 0, len(arr) - 1
        ans = len(arr)  # default insertion at end

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                # mid can be an answer, try to find an earlier position
                ans = mid
                high = mid - 1
            else:
                # need bigger value, go right
                low = mid + 1

        return ans

    def searchInsert(self, arr: List[int], target: int) -> int:
        """
        LeetCode: Search Insert Position

        Return the index where `target` should be inserted to keep the array sorted.
        This is exactly the LOWER BOUND:
            first index where arr[idx] >= target

        Example:
        arr = [1,3,5,6]
        target=5  -> 2
        target=2  -> 1
        target=7  -> 4
        """
        return self.lowerBound(arr, target)
