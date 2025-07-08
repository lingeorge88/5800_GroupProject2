# GROUP: 6
# MEMBERS: George Lin, Andrew Li, Xiaoti Hu, Minda Xie
# DATE: 07-12-2025
# ASSIGNMENT: Max Increase to Keep City Skyline Solution Implementation

from typing import List

"""
807. Max Increase to Keep City Skyline
There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.

A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.
"""


class Solution:
    def maxIncreaseKeepingSkyline1(self, grid: List[List[int]]) -> int:

        # find length of the grid
        n = len(grid)

        # find the max in each row
        rowMax = [0] * n
        for i in range(n):
            rowMax[i] = max(grid[i])

        # find the max in each column
        colMax = [0] * n
        for j in range(n):
            colMax[j] = max(grid[i][j] for i in range(n))

        # store the total increase
        totalIncrease = 0
        for i in range(n):
            for j in range(n):
                # find the maximum possible height this building can increase by without changing the skyline
                maxPossibleHeight = min(rowMax[i], colMax[j])

                # current height of the building
                currentHeight = grid[i][j]

                # we can only increase by the difference
                increase = maxPossibleHeight - currentHeight

                # add this increase to the total increase
                totalIncrease += increase
        # return the total increase
        return totalIncrease

    def maxIncreaseKeepingSkyline2(self, grid: List[List[int]]) -> int:
        """
        cleaner version of the solution above where we only traverse the grid twice instead of 3 times
        """
        # define length of the grid, row and col max
        n = len(grid)
        rowMax = [0] * n
        colMax = [0] * n

        # Calculate both row and column maxes in one pass
        for i in range(n):
            for j in range(n):
                rowMax[i] = max(rowMax[i], grid[i][j])
                colMax[j] = max(colMax[j], grid[i][j])

        # PRINT FOR code demo
        print(f"row maxes:{rowMax}")
        print(f"column maxes:{colMax}")

        # Calculate total increase
        totalIncrease = 0
        for i in range(n):
            for j in range(n):
                print(
                    f"row max at row {i}: {rowMax[i]}; column max at col {j}: {colMax[j]}\n"
                    f"current building height:{grid[i][j]}, available increase: {min(rowMax[i], colMax[j]) - grid[i][j]}"
                )
                totalIncrease += min(rowMax[i], colMax[j]) - grid[i][j]
                print(f"increase: {totalIncrease}")
        # return total increase
        return totalIncrease

    def maxIncreaseKeepingSkyline3(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def preservesSkyline(newGrid):
            # Check if new grid has same skyline as original
            for i in range(n):
                if max(newGrid[i]) != max(grid[i]):  # Row skyline changed
                    return False
            for j in range(n):
                if max(newGrid[i][j] for i in range(n)) != max(
                    grid[i][j] for i in range(n)
                ):
                    return False  # Column skyline changed
            return True

        maxIncrease = 0

        # Try all possible combinations of increases
        def generateAllCombinations(pos, currentGrid, totalIncrease):
            nonlocal maxIncrease

            if pos == n * n:
                if preservesSkyline(currentGrid):
                    maxIncrease = max(maxIncrease, totalIncrease)
                return

            i, j = pos // n, pos % n

            # Try increasing this building by 0, 1, 2, ..., up to reasonable limit
            for increase in range(10):  # Arbitrary limit
                currentGrid[i][j] += increase
                generateAllCombinations(pos + 1, currentGrid, totalIncrease + increase)
                currentGrid[i][j] -= increase  # Backtrack

        generateAllCombinations(0, [row[:] for row in grid], 0)
        return maxIncrease


def main():
    grid1 = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    solution = Solution()

    sol1 = solution.maxIncreaseKeepingSkyline1(grid1)
    sol2 = solution.maxIncreaseKeepingSkyline2(grid1)

    # sol3 = solution.maxIncreaseKeepingSkyline3(grid1)

    print(f"sol1:{sol1}, sol2:{sol2}, all solutions match?:{sol1 == sol2}")

    grid2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    sol_zero_1 = solution.maxIncreaseKeepingSkyline1(grid2)
    sol_zero_2 = solution.maxIncreaseKeepingSkyline2(grid2)
    print(
        f"sol1_zero:{sol_zero_1}, sol2_zero:{sol_zero_2}, all solutions match?:{sol_zero_1 == sol_zero_2}"
    )


if __name__ == "__main__":
    main()
