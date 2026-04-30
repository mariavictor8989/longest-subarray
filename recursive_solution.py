def is_balanced(sub):
    return sub.count(0) == sub.count(1)


def find_max_length_recursive(nums, start, end):
    if start >= end:
        return 0

    if is_balanced(nums[start:end + 1]):
        return end - start + 1

    return max(find_max_length_recursive(nums, start + 1, end),
               find_max_length_recursive(nums, start, end - 1))


# Example Test
if __name__ == "__main__":
    test_nums = [0, 0, 1, 0, 1, 1, 0]
    print(f"Longest Balanced Subarray (Recursive): {find_max_length_recursive(test_nums, 0, len(test_nums) - 1)}")