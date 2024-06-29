from app.date_converter.date_converter import DateConverter
from app.ip_address.ip_address import IPAddress
from app.text_handler.camel_case_parser import CamelCaseParser
from app.text_handler.text_handler import TextHandler

if __name__ == "__main__":

    text = TextHandler(
        (
            "A traditional critical review includes an introduction summarizing the key details of the work being "
            "reviewed, the body containing the evaluation, and a conclusion summarizing the review. "
            "Instructional texts usually start with an overview of the task or goal, and possibly, "
            "what the end result should look like."
        )
    )

    # 1 Task: Write a Python program that matches a word containing 'z', not the start or end of the word
    SEARCHED_CHAR = "z"
    word = text.match_word_containing_char(SEARCHED_CHAR)
    print(f"A word containing '{SEARCHED_CHAR}': ", word)
    # 2 Task: Write a Python program to remove leading zeros from an IP address
    ipaddress_obj = IPAddress("216.08.094.196")
    new_ipaddress = ipaddress_obj.remove_lead_zeros()
    print("Removed leading zeros from an IP address: ", new_ipaddress)
    # 3 Task: Write a Python program to find the occurrence and position of substrings within
    # a string (використайте атрбути знайденої групи).
    SUBSTRING_TEXT = "summarizing"
    for n, item in enumerate(text.find_substring(SUBSTRING_TEXT), 1):
        print(f"Substring {n}:", item)
    # 4 Task: Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format
    converter = DateConverter("2020-11-20")
    new_date = converter.change_date_format()
    print("Changed date format: ", new_date)
    # 5 Task: Write a Python program to find all three, four, and five character words in a string
    start_word_length, end_word_length = 3, 5
    words = text.find_all_words(start_word_length, end_word_length)
    print("All three, four, and five character words: ", words)
    # 6 Task: Write a Python program to convert a camel-case string to a snake-case string
    camel_case_str = CamelCaseParser("TextExercise")
    snake_case_str = camel_case_str.to_snake()
    print("Converted a camel-case to a snake-case: ", snake_case_str)
    # 7 Task: Write a Python program to find all adverbs and their positions in a given sentence
    adverbs = text.find_all_adverbs()
    for n, adverb in enumerate(adverbs, 1):
        print(f"Adverb {n}: ", adverb)
    # 8 Task: Write a Python program to concatenate the consecutive numbers in a given string.
    text = TextHandler(
        "Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. "
        "Please have your identification ready."
    )
    text.concatenate_numbers()
    print("Concatenated the consecutive numbers:\n", text.text)
