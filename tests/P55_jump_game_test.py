from leetcode_python.solutions.P55_jump_game import JumpGame


def test_jump_game_reachable_example() -> None:
    jump_game = JumpGame()
    assert jump_game.can_jump([2, 3, 1, 1, 4]) is True


def test_jump_game_unreachable_example() -> None:
    jump_game = JumpGame()
    assert jump_game.can_jump([3, 2, 1, 0, 4]) is False


def test_jump_game_handles_small_inputs() -> None:
    jump_game = JumpGame()

    assert jump_game.can_jump([0]) is True
    assert jump_game.can_jump([2, 0, 0]) is True
    assert jump_game.can_jump([1, 0, 1, 0]) is False
