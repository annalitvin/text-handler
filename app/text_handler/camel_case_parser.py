import re


class CamelCaseParser:
    CAMEL_CASE_FORMAT_ERROR_MSG = "Please provide the text in camel case format e.g. TextExercises"

    def __init__(self, input_text: str):
        self.text = input_text
        if not self.__check_if_str_camel_case():
            raise ValueError(self.CAMEL_CASE_FORMAT_ERROR_MSG)

    def __check_if_str_camel_case(self):
        pattern = "^[a-zA-Z]+([A-Z][a-z]+)+$"
        return bool(re.match(pattern, self.text))

    def to_snake(self):
        """Convert a camel-case string to a snake-case string.
        Ex. PythonExercise to python_exercise"""
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", self.text).lower()


if __name__ == "__main__":
    camel_case_str = CamelCaseParser("TextExercise")
    assert camel_case_str.to_snake() == "text_exercise"
