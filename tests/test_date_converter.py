import pytest

from app.date_converter.date_converter import DateConverter


class TestDateConverter:
    DATE_FORMAT_ERROR_MSG = "Please provide the date in yyyy-mm-dd format"

    @pytest.mark.parametrize(
        "date,expected",
        [
            ("2020-11-20", "20-11-2020"),
            ("1985-02-20", "20-02-1985"),
        ],
    )
    def test_change_date_format(self, date, expected):
        converter = DateConverter(date)
        assert converter.change_date_format() == expected

    @pytest.mark.parametrize(
        "date",
        [
            "2020/11/20",
            "1985.02.20",
        ],
    )
    def test_incorrect_date_format(self, date):
        with pytest.raises(ValueError) as error:
            DateConverter(date)
        assert self.DATE_FORMAT_ERROR_MSG in str(error.value)
