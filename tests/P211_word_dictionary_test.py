from leetcode_python.solutions.P211_word_dictionary import Trie


def test_word_dictionary_example() -> None:
    word_dictionary = Trie()

    word_dictionary.addWord("bad")
    word_dictionary.addWord("dad")
    word_dictionary.addWord("mad")

    assert word_dictionary.search("pad") is False
    assert word_dictionary.search("bad") is True
    assert word_dictionary.search(".ad") is True
    assert word_dictionary.search("b..") is True


def test_word_dictionary_rejects_partial_matches() -> None:
    word_dictionary = Trie()

    word_dictionary.addWord("app")

    assert word_dictionary.search("ap") is False
    assert word_dictionary.search("app") is True
    assert word_dictionary.search("ap.") is True


def test_word_dictionary_handles_multiple_wildcards() -> None:
    word_dictionary = Trie()

    word_dictionary.addWord("at")
    word_dictionary.addWord("and")
    word_dictionary.addWord("an")
    word_dictionary.addWord("add")

    assert word_dictionary.search("a.") is True
    assert word_dictionary.search("an.") is True
    assert word_dictionary.search("...") is True
    assert word_dictionary.search("....") is False
