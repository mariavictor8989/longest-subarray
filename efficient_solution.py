def find_max_length_efficient(nums):
    count_map = {0: -1}
    max_len = 0
    curr_sum = 0

    for i, num in enumerate(nums):
        curr_sum += 1 if num == 1 else -1

        if curr_sum in count_map:
            max_len = max(max_len, i - count_map[curr_sum])
        else:
            count_map[curr_sum] = i

    return max_len

if __name__ == "__main__":
    print("--- Longest Balanced Subarray Finder ---")
    try:
        user_input = input("Enter the binary array (0s and 1s) separated by spaces: ")

        test_nums = [int(x) for x in user_input.split()]

        if all(num in [0, 1] for num in test_nums):
            result = find_max_length_efficient(test_nums)
            print(f"\nTarget Array: {test_nums}")
            print(f"Result -> Longest Balanced Subarray Length: {result}")
        else:
            print("Error: Please enter only 0s and 1s.")

    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")