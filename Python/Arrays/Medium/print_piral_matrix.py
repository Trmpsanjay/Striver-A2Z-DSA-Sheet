from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Spiral traversal using 4 boundaries.

        How boundaries are calculated:
        - top    = 0                 (first row index)
        - bottom = len(matrix) - 1   (last row index)
        - left   = 0                 (first col index)
        - right  = len(matrix[0]) - 1(last col index)

        Meaning:
        - top..bottom = rows still not printed
        - left..right = cols still not printed

        After printing one side, we "shrink" that side inward:
        - printed top row    -> top += 1
        - printed right col  -> right -= 1
        - printed bottom row -> bottom -= 1
        - printed left col   -> left += 1

        We keep looping while a valid rectangle exists:
        - top <= bottom and left <= right
        """

        ans = []

        # boundaries of the current unvisited rectangle
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # 1) Traverse TOP boundary row (left -> right)
            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1  # top row done, move boundary down

            # 2) Traverse RIGHT boundary col (top -> bottom)
            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1  # right col done, move boundary left

            # 3) Traverse BOTTOM boundary row (right -> left) if rows remain
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1  # bottom row done, move boundary up

            # 4) Traverse LEFT boundary col (bottom -> top) if cols remain
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                left += 1  # left col done, move boundary right

        return ans
