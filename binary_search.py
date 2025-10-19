def binary_search(nums: List[int], x: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        pos = (left + right) // 2
        if nums[pos] == x:
            return pos
        elif nums[pos] > x:
            right = pos - 1
        else:
            left = pos + 1
    return -1

      