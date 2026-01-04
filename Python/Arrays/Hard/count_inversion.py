class Solution:

    def merge(self, arr, low, mid, high):
        """
        Merge two sorted halves:
          left  = arr[low .. mid]
          right = arr[mid+1 .. high]

        Intuition for inversions:
        - Inversion = (i < j) and arr[i] > arr[j]
        - During merge, if arr[left] <= arr[right], no inversion added.
        - If arr[left] > arr[right]:
            then arr[right] is smaller than ALL remaining elements from left..mid
            (because left half is sorted),
            so it forms (mid - left + 1) inversions at once.
        """
        temp = []
        left = low
        right = mid + 1
        cnt = 0  # inversion count in this merge step

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                # arr[right] is smaller than arr[left..mid] => all are inversions
                cnt += (mid - left + 1)
                right += 1

        # copy leftovers
        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        # write merged sorted segment back
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return cnt

    def mergeSort(self, arr, low, high):
        """
        Standard merge sort, but also counts inversions.

        Intuition:
        - Total inversions =
            inversions in left half
          + inversions in right half
          + inversions across halves (counted during merge)

        Why merge sort helps:
        - Brute force checks all pairs => O(n^2)
        - Merge sort splits + counts cross inversions efficiently => O(n log n)
        """
        cnt = 0
        if low >= high:
            return 0

        mid = (low + high) // 2

        cnt += self.mergeSort(arr, low, mid)        # left inversions
        cnt += self.mergeSort(arr, mid + 1, high)   # right inversions
        cnt += self.merge(arr, low, mid, high)      # cross inversions

        return cnt

    def inversionCount(self, arr):
        """
        Return number of inversions in the array.

        Layman / real-life intuition:
        - Think of people in a line by height.
        - An inversion is a "taller person standing before a shorter person" (out of order).
        - Merge sort counts how many such out-of-order pairs exist while sorting.
        """
        return self.mergeSort(arr, 0, len(arr) - 1)
