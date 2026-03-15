"""Problem 1: Two Sum."""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices of the two numbers whose sum equals target."""
    seen: dict[int, int] = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

    raise ValueError("No solution found")
