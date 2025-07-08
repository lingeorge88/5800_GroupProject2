import time
import matplotlib.pyplot as plt
import random
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)
        return maxarea

    def maxArea1(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea

def generate_test_data(size):
    return [random.randint(1, 10000) for _ in range(size)]

def run_complexity_analysis():
    solution = Solution()
    
    input_sizes = [100, 200, 500, 1000, 2000, 5000]
    
    large_sizes = [10000, 20000, 50000, 100000]
    
    times_brute = []
    times_optimized = []
    times_optimized_large = []
    
    print("Testing both algorithms on smaller input sizes:")
    print("=" * 60)
    
    for size in input_sizes:
        print(f"Testing size {size}...")
        
        test_data = generate_test_data(size)
        
        start = time.perf_counter()
        result1 = solution.maxArea(test_data)
        time_brute = time.perf_counter() - start
        times_brute.append(time_brute)
        
        start = time.perf_counter()
        result2 = solution.maxArea1(test_data)
        time_optimized = time.perf_counter() - start
        times_optimized.append(time_optimized)
        
        assert result1 == result2, f"Results don't match! Brute: {result1}, Optimized: {result2}"
        
        print(f"  Brute Force: {time_brute:.6f}s")
        print(f"  Two-Pointer: {time_optimized:.6f}s")
        print(f"  Speedup: {time_brute/time_optimized:.2f}x")
        print()
    
    print("Testing optimized algorithm on larger input sizes:")
    print("=" * 60)
    
    for size in large_sizes:
        print(f"Testing size {size}...")
        
        test_data = generate_test_data(size)
        
        start = time.perf_counter()
        result = solution.maxArea1(test_data)
        time_optimized_large = time.perf_counter() - start
        times_optimized_large.append(time_optimized_large)
        
        print(f"  Two-Pointer: {time_optimized_large:.6f}s")
        print()
    
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, times_brute, label="Brute Force O(n²)", marker="o", color='red')
    plt.plot(input_sizes, times_optimized, label="Two-Pointer O(n)", marker="o", color='blue')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Algorithm Comparison: Small to Medium Sizes")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    
    plt.subplot(1, 2, 2)
    all_sizes = input_sizes + large_sizes
    all_times = times_optimized + times_optimized_large
    plt.plot(all_sizes, all_times, label="Two-Pointer O(n)", marker="o", color='blue')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Two-Pointer Algorithm: Scaling to Large Sizes")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"Brute Force Algorithm:")
    print(f"  - Time Complexity: O(n²)")
    print(f"  - Space Complexity: O(1)")
    print(f"  - Largest tested size: {max(input_sizes)} elements")
    print(f"  - Max execution time: {max(times_brute):.6f}s")
    print()
    print(f"Two-Pointer Algorithm:")
    print(f"  - Time Complexity: O(n)")
    print(f"  - Space Complexity: O(1)")
    print(f"  - Largest tested size: {max(large_sizes)} elements")
    print(f"  - Max execution time: {max(all_times):.6f}s")
    print()
    print(f"Performance Improvement:")
    avg_speedup = sum(times_brute[i]/times_optimized[i] for i in range(len(times_brute))) / len(times_brute)
    print(f"  - Average speedup: {avg_speedup:.2f}x")
    print(f"  - Best speedup: {max(times_brute[i]/times_optimized[i] for i in range(len(times_brute))):.2f}x")

if __name__ == "__main__":
    run_complexity_analysis()