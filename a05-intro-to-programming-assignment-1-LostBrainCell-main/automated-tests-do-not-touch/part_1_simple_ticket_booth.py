from io import StringIO
import sys
from unittest.mock import patch
from unittest import mock
import difflib
import runpy

FILE_NAME = "simple_ticket_booth.py"


def run_file_with_patches(user_input_patches=None, mystery_discount=3):
    if user_input_patches is None:
        user_input_patches = []

    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate user input and run the file
    with patch("builtins.input", side_effect=user_input_patches):
        # mystery_discount = random.randint(1, 5)
        with mock.patch("random.randint", return_value=mystery_discount):
            runpy.run_path(FILE_NAME)
    # Get the value of the captured output
    output = captured_output.getvalue().strip().split("\n")
    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
    return output


def assert_similar_string(a, b, threshold=0.91):
    similarity = difflib.SequenceMatcher(None, a, b).ratio()
    assert similarity >= threshold, f"Strings '{a}' and '{b}' are not similar enough!"


def get_output_string_than_starts_with(output, starts_with):
    for line in output:
        if line.lower().startswith(starts_with.lower()):
            return line
    raise ValueError(f"No line starts with '{starts_with}'")


def test_no_ticket():
    output = run_file_with_patches(user_input_patches=["no"])
    last_line = get_output_string_than_starts_with(output, "Thanks")
    assert_similar_string(last_line, "Thanks, maybe next time")


def test_invalid_input():
    output = run_file_with_patches(user_input_patches=["potato"])
    last_line = get_output_string_than_starts_with(output, "Invalid input")
    assert_similar_string(last_line, "Invalid input, Please try again")


def test_free_ticket():
    # age under 5 -> free, no coupon question
    output = run_file_with_patches(user_input_patches=["yes", "4"])
    last_line = get_output_string_than_starts_with(output, "Your ticket is free")
    assert_similar_string(last_line, "Your ticket is free")


def test_child_with_coupon():
    # 12.00 base - 5.00 coupon - 3.00 mystery = 4.00
    output = run_file_with_patches(
        user_input_patches=["yes", "10", "yes"], mystery_discount=3
    )
    price_line = get_output_string_than_starts_with(output, "Your ticket costs")
    assert "$4.00" in price_line


def test_adult_without_coupon():
    # 25.00 base - 4.00 mystery = 21.00
    output = run_file_with_patches(
        user_input_patches=["yes", "30", "no"], mystery_discount=4
    )
    price_line = get_output_string_than_starts_with(output, "Your ticket costs")
    assert "$21.00" in price_line


def test_senior_with_coupon():
    # 15.00 base - 5.00 coupon - 2.00 mystery = 8.00
    output = run_file_with_patches(
        user_input_patches=["yes", "70", "yes"], mystery_discount=2
    )
    price_line = get_output_string_than_starts_with(output, "Your ticket costs")
    assert "$8.00" in price_line


if __name__ == "__main__":
    test_no_ticket()
    test_invalid_input()
    test_free_ticket()
    test_child_with_coupon()
    test_adult_without_coupon()
    test_senior_with_coupon()
    # if the above fail they will make the output not successful and throw an error.
    print("successful output")
