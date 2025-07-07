from typing import List

class Solution:
    # Brute-force solution: O(n^2) time complexity
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                # Area = min height * width
                maxarea = max(maxarea, min(height[left], height[right]) * width)
        return maxarea

    # Optimized two-pointer solution: O(n) time complexity
    def maxArea1(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            # Calculate area based on shorter line
            maxarea = max(maxarea, min(height[left], height[right]) * width)

            # Move the pointer pointing to the shorter line
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea

# ----- Test Cases -----

def run_tests():
    solution = Solution()

    test_cases = [
        ([1,8,6,2,5,4,8,3,7], 49),  # tallest on both ends
        ([1,1], 1),                # simple case, only 2 bars
        ([4,3,2,1,4], 16),         # max between two ends
        ([1,2,1], 2),              # max in the middle
        ([2,3,4,5,18,17,6], 17),   # max with distant high bars
    ]

    for i, (heights, expected) in enumerate(test_cases):
        result1 = solution.maxArea(heights)
        result2 = solution.maxArea1(heights)
        print(f"Test Case {i + 1}:")
        print(f"  Input: {heights}")
        print(f"  Expected: {expected}")
        print(f"  Brute Force Result: {result1} " if result1 == expected else f"   Brute Force Result: {result1}")
        print(f"  Two Pointer Result: {result2} " if result2 == expected else f"   Two Pointer Result: {result2}")
        print()

# Run all the tests
run_tests()
