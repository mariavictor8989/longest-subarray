def is_balanced(sub):
    return sub.count(0) == sub.count(1)


def find_max_length_recursive(nums, start, end):
    if start >= end:
        return 0

    if is_balanced(nums[start:end + 1]):
        return end - start + 1

    return max(find_max_length_recursive(nums, start + 1, end),
               find_max_length_recursive(nums, start, end - 1))


if __name__ == "__main__":
    print("--- Longest Balanced Subarray (Recursive Approach) ---")
    try:
        user_input = input("Enter the binary array (0s and 1s) separated by spaces: ")
        test_nums = [int(x) for x in user_input.split()]

        if all(num in [0, 1] for num in test_nums):
            result = find_max_length_recursive(test_nums, 0, len(test_nums) - 1)
            print(f"\nTarget Array: {test_nums}")
            print(f"Result -> Longest Balanced Subarray Length: {result}")
        else:
            print("Error: Please enter only 0s and 1s.")

    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")