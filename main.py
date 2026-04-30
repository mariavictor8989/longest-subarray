def find_max_length_non_recursive(nums):
    storage = {0: -1}
    max_length = 0
    current_sum = 0
    for i in range(len(nums)):
        current_sum += 1 if nums[i] == 1 else -1
        if current_sum in storage:
            max_length = max(max_length, i - storage[current_sum])
        else:
            storage[current_sum] = i
    return max_length
