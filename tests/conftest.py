import pytest

from app.text_handler.text_handler import TextHandler

TEXT = (
    "A traditional critical review includes an introduction summarizing the key details of the work being "
    "reviewed, the body containing the evaluation, and a conclusion summarizing the review. "
    "Instructional texts usually start with an overview of the task or goal, and possibly, "
    "what the end result should look like."
)


@pytest.fixture(params=[TEXT])
def text_handler(request):
    return TextHandler(request.param)
