from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # We use FIRST ROW and FIRST COLUMN as "markers/notebook" later:
        # - matrix[r][0] == 0  => row r should become all zeros
        # - matrix[0][c] == 0  => col c should become all zeros
        #
        # Problem: while marking, we may turn cells in first row/col into 0
        # even if they were NOT originally 0.
        # So we store the ORIGINAL info in two extra booleans:
        row0_has_zero = any(matrix[0][c] == 0 for c in range(cols))  # was there a 0 in first row originally?
        col0_has_zero = any(matrix[r][0] == 0 for r in range(rows))  # was there a 0 in first col originally?

        # Mark rows/cols using first row/col (start from 1 to avoid corrupting markers early)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # mark row r
                    matrix[0][c] = 0  # mark col c

        # Zero out marked rows (skip first row for now)
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        # Zero out marked cols (skip first col for now)
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0

        # Finally, handle first row/col using saved ORIGINAL info
        if row0_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if col0_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
