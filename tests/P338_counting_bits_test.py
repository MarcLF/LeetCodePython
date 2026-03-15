import pytest
from leetcode_python.solutions.P338_counting_bits import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, [0]),
        (1, [0, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
    ],
)
def test_count_bits(n, expected):
    sol = Solution()
    assert sol.count_bits(n) == expected
