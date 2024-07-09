import pytest

from app.text_handler.camel_case_parser import CamelCaseParser


class TestCamelCaseParser:
    CAMEL_CASE_FORMAT_ERROR_MSG = "Please provide the text in camel case format"

    @pytest.mark.parametrize(
        "camel_case_str,expected",
        [
            ("TextExercise", "text_exercise"),
        ],
    )
    def test_to_snake(self, camel_case_str, expected):
        camel_case_obj = CamelCaseParser(camel_case_str)
        assert camel_case_obj.to_snake() == expected

    @pytest.mark.parametrize(
        "camel_case_str",
        [
            "I love salad",
        ],
    )
    def test_incorrect_date_format(self, camel_case_str):
        with pytest.raises(ValueError) as error:
            CamelCaseParser(camel_case_str)
        assert self.CAMEL_CASE_FORMAT_ERROR_MSG in str(error.value)
