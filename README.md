# Longest Balanced Subarray Project 🚀

This project provides two solutions to find the maximum length of a contiguous subarray with an equal number of 0s and 1s.

##  Problem Description
Given a binary array, we need to find the longest subarray where the count of 0s equals the count of 1s.
- **Example**: Input `[0, 0, 1, 0, 1, 1, 0]` -> Output `6`

##  Features
- **Interactive Input**: Users can enter their own binary arrays via the console.
- **Two Approaches**:
  1. **Efficient Solution ($O(n)$)**: Uses a Hash Map (Dictionary) and a cumulative sum technique (treating 0 as -1).
  2. **Recursive Solution**: A classical divide-and-conquer approach to understand the logic.

## How to Run
1. Run `efficient_solution.py` for the fast approach.
2. Run `recursive_solution.py` for the recursive approach.
3. Enter your numbers separated by spaces (e.g., `0 1 0 1`).
