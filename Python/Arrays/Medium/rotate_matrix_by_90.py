from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        LeetCode: Rotate Image
        https://leetcode.com/problems/rotate-image/

        Task:
        - Rotate the n x n matrix by 90 degrees clockwise, IN-PLACE.

        Easy memory trick:
        ✅ "TRANSPOSE + REVERSE each ROW"  => 90° clockwise

        Why it works (super simple):
        1) Transpose flips across the main diagonal (row <-> col).
        2) Reversing each row turns that into a clockwise rotation.

        Complexity:
        - Time: O(n^2)
        - Extra Space: O(1) (in-place)

        Common mistakes:
        - Swapping whole transpose twice: start inner loop from j=i+1.
        - Reversing columns instead of rows (that would rotate counterclockwise).
        - Works only for square matrix (n x n) as per problem.
        """

        n = len(matrix)

        # 1) TRANSPOSE: swap matrix[i][j] with matrix[j][i] for j > i
        # (j starts from i+1 to avoid swapping diagonal and double-swapping)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2) REVERSE EACH ROW: completes the 90° clockwise rotation
        for i in range(n):
            matrix[i] = matrix[i][::-1]
