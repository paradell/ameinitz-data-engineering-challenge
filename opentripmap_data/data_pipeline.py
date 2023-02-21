from datetime import datetime

from data_extraction import extract_data_from_opentripmap_to_df
from data_loading import store_dataframe_as_csv_file
from data_transformation import add_kinds_amount_column
from data_transformation import filter_by_skyscrappers_accommodations

TODAY_DATE = datetime.strftime(datetime.now(), "%Y-%m-%d")
OUTPUT_FILE_PATH = "output_files"
OUTPUT_FILE_NAME = f"skyscrappers_bcn_{TODAY_DATE}.csv"

# Extract data and store it in a Pandas DataFrame
locations_df = extract_data_from_opentripmap_to_df()

# Add a new column with the number of kinds each accommodation has
locations_df = add_kinds_amount_column(locations_df)

# Filter by skyscrapper accommodation
skyscrapper_df = filter_by_skyscrappers_accommodations(locations_df)

# Store dataframe as CSV file
store_dataframe_as_csv_file(
    dataframe=skyscrapper_df, output_file=f"{OUTPUT_FILE_PATH}/{OUTPUT_FILE_NAME}"
)
