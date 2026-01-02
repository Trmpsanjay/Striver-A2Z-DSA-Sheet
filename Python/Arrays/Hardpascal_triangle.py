from typing import List

class Solution:
    """
    Pascal's Triangle (LeetCode 118)

    Goal:
    - Build the first `numRows` of Pascal’s Triangle.

    Key pattern to remember (very easy):
    ✅ Each row can be generated using the formula:
       next_val = prev_val * (row - col) / col

    Where:
    - row is 1-based (row = 1 gives [1])
    - col goes from 1 to row-1 (also 1-based for this formula)

    Real-life analogy:
    - Think of making a row as a "recipe":
      you start with 1, then each next ingredient is computed from the previous one
      using a small multiply + divide (no need to compute factorials).

    Complexity:
    - Time: O(numRows^2) (because total elements are 1+2+...+numRows)
    - Space: O(numRows^2) for output

    Common pain points / mistakes:
    1) Confusing row indexing:
       - Here `row` is 1-based.
       - row=1 -> [1]
       - row=2 -> [1, 1]
    2) Using float division:
       - Must use integer division (//) because results are always integers.
    3) Wrong update order:
       - Update ans using previous ans, then append.
    """

    def generate_row(self, row: int) -> List[int]:
        """
        Generate a single row of Pascal's triangle (1-based row index).

        Example:
        row = 1 -> [1]
        row = 4 -> [1, 3, 3, 1]

        How it works:
        - Start with 1.
        - Each next value is derived from previous value:
            ans = ans * (row - col) // col
        """
        ans = 1              # first element of every row is 1
        result = [1]         # store row values

        # col runs from 1 to row-1
        for col in range(1, row):
            # Compute next value from previous value
            # next = prev * (row-col) / col
            ans = ans * (row - col)
            ans = ans // col
            result.append(ans)

        return result

    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generate Pascal's triangle up to numRows.

        Build row-by-row using generate_row().
        """
        result = []
        for row in range(1, numRows + 1):   # row is 1-based
            result.append(self.generate_row(row))
        return result
