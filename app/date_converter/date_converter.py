import re


class DateConverter:
    DATE_REGEX = re.compile(r"(\d{4})-(0[1-9]|1[0,1,2])-(0[1-9]|[12][0-9]|3[01])")
    DATE_FORMAT_ERROR_MSG = "Please provide the date in yyyy-mm-dd format"

    def __init__(self, date: str):
        self.__date: str = date
        if not self.__check_if_date_format_valid(self.DATE_REGEX):
            raise ValueError(self.DATE_FORMAT_ERROR_MSG)

    @property
    def date(self):
        return self.__date

    def __check_if_date_format_valid(self, date_pattern: re.Pattern):
        """Checks that the date is in the yyyy-mm-dd format."""
        return bool(re.match(date_pattern, self.__date))

    def change_date_format(self):
        """Convert a date of yyyy-mm-dd format to dd-mm-yyyy format"""
        return re.sub(self.DATE_REGEX, "\\3-\\2-\\1", self.__date)


if __name__ == "__main__":
    converter = DateConverter("2020-11-20")
    assert converter.change_date_format() == "20-11-2020"
