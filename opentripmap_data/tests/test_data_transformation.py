import sys

import pandas as pd
from pandas.testing import assert_frame_equal

sys.path.append("..")

from opentripmap_data.data_transformation import (
    add_kinds_amount_column,
    filter_by_skyscrappers_accommodations,
)


# Test add_kinds_amount_column
def test_add_kinds_amount_column():
    input_df = pd.DataFrame(
        {
            "id": [0, 1, 2],
            "kinds": ["accomodations,other_hotels", "accomodations", "beach,sun,sea"],
        }
    )
    expected_df = pd.DataFrame(
        {
            "id": [0, 1, 2],
            "kinds": ["accomodations,other_hotels", "accomodations", "beach,sun,sea"],
            "kinds_amount": [2, 1, 3],
        }
    )
    assert_frame_equal(add_kinds_amount_column(input_df), expected_df)


def test_add_kinds_amount_column_empty_string():
    input_df = pd.DataFrame({"id": [0], "kinds": [""]})
    expected_df = pd.DataFrame({"id": [0], "kinds": [""], "kinds_amount": [1]})
    assert_frame_equal(add_kinds_amount_column(input_df), expected_df)


# Test filter_by_skyscrappers_accommodations
def test_filter_by_skyscrappers_accommodations():
    input_df = pd.DataFrame(
        {
            "id": [0, 1, 2],
            "kinds": [
                "accomodations,skyscrapers",
                "accomodations",
                "skyscrapers,sun,sea",
            ],
        }
    )
    expected_df = pd.DataFrame(
        {"id": [0, 2], "kinds": ["accomodations,skyscrapers", "skyscrapers,sun,sea"]}
    )
    assert_frame_equal(
        filter_by_skyscrappers_accommodations(input_df).reset_index(drop=True),
        expected_df,
    )


def test_filter_by_skyscrappers_accommodations_no_skyscrapper():
    input_df = pd.DataFrame(
        {"id": [0, 1, 2], "kinds": ["accomodations", "accomodations", "sun,sea"]}
    )
    expected_df = pd.DataFrame({"id": [], "kinds": []})
    assert_frame_equal(
        filter_by_skyscrappers_accommodations(input_df).reset_index(drop=True),
        expected_df,
        check_dtype=False,
    )
