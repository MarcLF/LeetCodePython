from leetcode_python.solutions.P208_trie import Trie


def test_trie_example() -> None:
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True

    trie.insert("app")
    assert trie.search("app") is True
