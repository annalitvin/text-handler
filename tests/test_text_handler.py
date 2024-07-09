import pytest


class TestTextHandler:
    SEARCHED_CHAR = "z"
    SUBSTRING_TEXT = "summarizing"

    def test_match_word_containing_char(self, text_handler):
        assert text_handler.match_word_containing_char(self.SEARCHED_CHAR) == "summarizing"

    def test_find_all_words(self, text_handler):
        start_word_length, end_word_length = 3, 5
        assert text_handler.find_all_words(start_word_length, end_word_length) == [
            "the",
            "key",
            "the",
            "work",
            "being",
            "the",
            "body",
            "the",
            "and",
            "the",
            "texts",
            "start",
            "with",
            "the",
            "task",
            "goal",
            "and",
            "what",
            "the",
            "end",
            "look",
            "like",
        ]

    def test_find_substring(self, text_handler):
        assert list(text_handler.find_substring(self.SUBSTRING_TEXT)) == [
            {"summarizing": (55, 66)},
            {"summarizing": (164, 175)},
        ]

    def test_find_all_adverbs(self, text_handler):
        assert list(text_handler.find_all_adverbs()) == [(208, 215, "usually"), (264, 272, "possibly")]

    @pytest.mark.parametrize(
        "text_handler",
        [
            (
                "Enter at 115 20 Kearny Street. The security desk can direct you to floor 1 6. "
                "Please have your identification ready."
            )
        ],
        indirect=True,
    )
    def test_concatenate_numbers(self, text_handler):
        text_handler.concatenate_numbers()
        assert text_handler.text == (
            "Enter at 11520 Kearny Street. "
            "The security desk can direct you to floor 16. Please have your identification ready."
        )
