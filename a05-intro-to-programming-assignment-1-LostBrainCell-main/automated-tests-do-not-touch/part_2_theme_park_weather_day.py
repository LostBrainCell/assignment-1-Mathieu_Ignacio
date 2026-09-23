from io import StringIO
import sys
from unittest.mock import patch
from unittest import mock
import difflib
import runpy

FILE_NAME = "theme_park_weather_day.py"

# Weather rating values used by random.randint(1, 3)
SUNNY = 1
RAINY = 2
STORMY = 3


def run_file_with_patches(user_input_patches=None, mystery_discount=3, weather_rating=SUNNY):
    if user_input_patches is None:
        user_input_patches = []

    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate user input and run the file.
    # random.randint is called twice, in this order:
    #   mystery_discount = random.randint(1, 5)
    #   weather_rating   = random.randint(1, 3)
    with patch("builtins.input", side_effect=user_input_patches):
        with mock.patch("random.randint", side_effect=[mystery_discount, weather_rating]):
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


def test_adult_parking_snack_sunny():
    # ticket 25 - 2 mystery = 23; parking 10; snack 8; sunny no change -> 41.00
    output = run_file_with_patches(
        user_input_patches=["yes", "30", "no", "yes", "yes"],
        mystery_discount=2,
        weather_rating=SUNNY,
    )
    weather_line = get_output_string_than_starts_with(output, "Weather Description")
    assert_similar_string(weather_line, "Weather Description: Sunny")
    total_line = get_output_string_than_starts_with(output, "Your final total is")
    assert "$41.00" in total_line


def test_adult_snack_rainy():
    # ticket 25 - 5 mystery = 20; no parking; snack 8 -> half = 4; rainy -> 24.00
    output = run_file_with_patches(
        user_input_patches=["yes", "30", "no", "no", "yes"],
        mystery_discount=5,
        weather_rating=RAINY,
    )
    weather_line = get_output_string_than_starts_with(output, "Weather Description")
    assert_similar_string(weather_line, "Weather Description: Rainy")
    total_line = get_output_string_than_starts_with(output, "Your final total is")
    assert "$24.00" in total_line


def test_senior_coupon_parking_stormy():
    # ticket 15 - 5 coupon - 2 mystery = 8; parking 10 -> free; stormy -> 8.00
    output = run_file_with_patches(
        user_input_patches=["yes", "70", "yes", "yes", "no"],
        mystery_discount=2,
        weather_rating=STORMY,
    )
    weather_line = get_output_string_than_starts_with(output, "Weather Description")
    assert_similar_string(weather_line, "Weather Description: Stormy")
    total_line = get_output_string_than_starts_with(output, "Your final total is")
    assert "$8.00" in total_line


def test_free_ticket_with_snack():
    # age under 5 -> free; no parking; snack 8; sunny -> 8.00
    output = run_file_with_patches(
        user_input_patches=["yes", "4", "no", "yes"],
        weather_rating=SUNNY,
    )
    free_line = get_output_string_than_starts_with(output, "Your ticket is free")
    assert_similar_string(free_line, "Your ticket is free")
    total_line = get_output_string_than_starts_with(output, "Your final total is")
    assert "$8.00" in total_line


def test_invalid_input():
    output = run_file_with_patches(user_input_patches=["potato"])
    last_line = get_output_string_than_starts_with(output, "Invalid input")
    assert_similar_string(last_line, "Invalid input, Please try again")


if __name__ == "__main__":
    test_adult_parking_snack_sunny()
    test_adult_snack_rainy()
    test_senior_coupon_parking_stormy()
    test_free_ticket_with_snack()
    test_invalid_input()
    # if the above fail they will make the output not successful and throw an error.
    print("successful output")
