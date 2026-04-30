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


# Example Test
if __name__ == "__main__":
    test_nums = [0, 0, 1, 0, 1, 1, 0]
    print(f"Longest Balanced Subarray (Efficient): {find_max_length_efficient(test_nums)}")