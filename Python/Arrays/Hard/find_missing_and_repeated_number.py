from typing import List

class Solution:
    def findTwoElement(self, arr: List[int]) -> List[int]:
        """
        Find the repeating and the missing number in an array of size n
        containing numbers from 1..n (one number repeats, one number is missing).

        Returns:
            [repeating, missing]   (GFG format)

        Intuition (math with sums):
        - Let missing = x, repeating = y
        - Expected sum of 1..n:        S  = n(n+1)/2
        - Actual sum of array:         S'
          Then: S' = S - x + y  =>  (S' - S) = y - x

        - Expected square sum of 1..n: SQ  = n(n+1)(2n+1)/6
        - Actual square sum:           SQ'
          Then: SQ' = SQ - x^2 + y^2  => (SQ' - SQ) = y^2 - x^2

        Use identity:
            y^2 - x^2 = (y - x)(y + x)

        So:
        - diff  = (S' - S)   = y - x
        - sqDiff= (SQ' - SQ) = (y - x)(y + x)
        - sumXY = (y + x)    = sqDiff / diff

        Solve:
        - y = (diff + sumXY) / 2
        - x = sumXY - y

        Complexity:
        - Time: O(n)
        - Space: O(1)

        Common pain points:
        - Mixing signs: diff here is (y - x), not (x - y)
        - Must compute (y + x) using sqDiff // diff before solving
        """

        arr_sum = 0
        arr_sq_sum = 0
        for num in arr:
            arr_sum += num
            arr_sq_sum += num * num

        n = len(arr)

        perfect_sum = n * (n + 1) // 2
        perfect_sqr_sum = n * (n + 1) * (2 * n + 1) // 6

        # diff = y - x
        diff = arr_sum - perfect_sum

        # sqDiff = y^2 - x^2
        sqDiff = arr_sq_sum - perfect_sqr_sum

        # sumXY = y + x
        sumXY = sqDiff // diff

        # repeating y and missing x
        y = (diff + sumXY) // 2
        x = sumXY - y

        return [y, x]
