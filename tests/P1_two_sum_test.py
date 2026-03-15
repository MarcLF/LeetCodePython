from leetcode_python.solutions.P1_two_sum import Solution


def test_two_sum_example() -> None:
    sol = Solution()
    assert sol.two_sum([2, 7, 11, 15], 9) == [0, 1]
