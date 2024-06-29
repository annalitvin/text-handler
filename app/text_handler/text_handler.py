import re


class TextHandler:

    def __init__(self, input_text: str):
        self.__text: str = input_text

    @property
    def text(self):
        return self.__text

    def match_word_containing_char(self, char: str):
        """Matches a word containing accepted char, not the start or end of the word."""
        pattern = rf"\b[^\s\\]+{char}[^\s\\]+\b"
        search = re.search(pattern, self.text)
        if search:
            return search.group()

    def concatenate_numbers(self) -> None:
        """Concatenate the consecutive numbers in a given text.
        Ex. 1 20 to 120."""
        self.__text = re.sub(r"(?<=\d)\s(?=\d)", "", self.text)

    def find_all_words(self, start: int, end: int):
        """Return all three, four, and five character words in a text."""
        pattern = r"\b\w{%s,%s}\b" % (start, end)
        return re.findall(pattern, self.text)

    def find_substring(self, sub: str):
        """Return the occurrence and position of substrings within a text."""
        for match in re.finditer(sub, self.__text):
            start, end = match.start(), match.end()
            word = self.__text[start:end]
            yield {word: (start, end)}

    def find_all_adverbs(self):
        """Return all adverbs and their positions in a given text."""
        for match in re.finditer(r"\w+ly", self.__text):
            start, end = match.start(), match.end()
            word = match.group(0)
            yield start, end, word


if __name__ == "__main__":
    text_handler = TextHandler(
        "A traditional critical review includes an introduction summarizing the key details of the work being "
        "reviewed, the body containing the evaluation, and a conclusion summarizing the review. "
        "Instructional texts usually start with an overview of the task or goal, and possibly, "
        "what the end result should look like."
    )
    assert text_handler.match_word_containing_char("z") == "summarizing"
    assert text_handler.find_all_words(3, 5) == [
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
    assert list(text_handler.find_substring("summarizing")) == [{"summarizing": (55, 66)}, {"summarizing": (164, 175)}]
    assert list(text_handler.find_all_adverbs()) == [(208, 215, "usually"), (264, 272, "possibly")]
    text = TextHandler(
        "Enter at 115 20 Kearny Street. The security desk can direct you to floor 1 6. "
        "Please have your identification ready."
    )
    text.concatenate_numbers()
    assert text.text == (
        "Enter at 11520 Kearny Street. "
        "The security desk can direct you to floor 16. Please have your identification ready."
    )
