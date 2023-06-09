def find_two_sum(nums: [int], target: int) -> [int]:
    for p1 in range(len(nums)):
        number_to_find = target - nums[p1]
        for p2 in range(p1 + 1, len(nums)):
            if number_to_find == nums[p2]:
                return [p1, p2]
    return None


def find_two_sum_opt(nums: [int], target: int) -> [int]:
    nums_map = {}

    for i, p1 in enumerate(nums):
        if p1 in nums_map:
            return [nums_map[p1], i]
        number_to_find = target - nums[i]
        nums_map[number_to_find] = i
    return None
