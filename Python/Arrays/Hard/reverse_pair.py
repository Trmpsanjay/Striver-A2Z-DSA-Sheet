from typing import List

class Solution:

    def merge(self, arr, low, mid, high):
        """
        Merge step for Reverse Pairs (LeetCode 493).

        This function does TWO things:
        1) Counts "cross" reverse pairs where:
              i is in left half  (low .. mid)
              j is in right half (mid+1 .. high)
           and arr[i] > 2 * arr[j]

        2) Merges the two sorted halves into one sorted segment.

        Key intuition:
        - After mergeSort recursion, BOTH halves are already sorted.
        - To count pairs efficiently, use two pointers:
            i walks the left half
            j walks the right half (only moves forward, never resets)
          For each i, all right elements before j satisfy the condition.

        Complexity of this merge step:
        - Counting: O(high-low+1) because j only moves forward overall
        - Merging:  O(high-low+1)
        """

        # ----- 1) COUNT reverse pairs across halves -----
        cnt = 0
        i = low
        j = mid + 1

        # For each element in left half, find how many elements in right half
        # satisfy arr[i] > 2 * arr[j]
        while i <= mid:
            # Move j as long as condition holds
            while j <= high and arr[i] > 2 * arr[j]:
                j += 1

            # All indices in right half from (mid+1) to (j-1) form reverse pairs with i
            cnt += (j - (mid + 1))
            i += 1

        # ----- 2) NORMAL MERGE (just sort the segment) -----
        temp = []
        left = low
        right = mid + 1

        # Standard merge of two sorted arrays
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Copy remaining elements
        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy merged result back into original array
        for idx in range(low, high + 1):
            arr[idx] = temp[idx - low]

        return cnt

    def mergeSort(self, arr, low, high):
        """
        Merge sort that returns the number of reverse pairs in arr[low..high].

        Total reverse pairs =
            reverse pairs in left half
          + reverse pairs in right half
          + cross reverse pairs (counted during merge)

        Time:  O(n log n)
        Space: O(n) for temp arrays during merge + O(log n) recursion stack
        """
        if low >= high:
            return 0

        mid = (low + high) // 2
        cnt = 0

        # Count in left half
        cnt += self.mergeSort(arr, low, mid)

        # Count in right half
        cnt += self.mergeSort(arr, mid + 1, high)

        # Count cross pairs + merge sorted halves
        cnt += self.merge(arr, low, mid, high)

        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        """
        LeetCode 493: Reverse Pairs

        Count pairs (i < j) such that:
            nums[i] > 2 * nums[j]

        Approach:
        - Use modified merge sort:
          * recursively sort halves
          * during merge, count cross reverse pairs using two pointers
          * then merge normally

        Time:  O(n log n)
        Space: O(n) extra (for merging)
        """
        return self.mergeSort(nums, 0, len(nums) - 1)
