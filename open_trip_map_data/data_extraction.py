# Extract 2500 entries from Open Trip Map
import os

from data_extraction_utils import extract_data
from data_extraction_utils import store_locations_in_dataframe

OPENTRIPMAP_URL = "https://api.opentripmap.com"
VERSION = "0.1"
LANGAUGE = "en"
ENDPOINT = "places/bbox"  # This challenge requires to get all accommodations inside a defined longitude and latitude
FORMAT = "json"
KINDS = "accomodations"
MIN_LONGITUDE = "2.028471"
MAX_LONGITUDE = "2.283903"
MIN_LATITUDE = "41.315758"
MAX_LATITUDE = "41.451768"
LIMIT = 2500

request_parameters = {
    "kinds": KINDS,
    "lon_min": MIN_LONGITUDE,
    "lon_max": MAX_LONGITUDE,
    "lat_min": MIN_LATITUDE,
    "lat_max": MAX_LATITUDE,
    "format": FORMAT,
    "limit": LIMIT,  # TODO - this parameter is not having any impact on the payload.
    "apikey": os.getenv("OPENTRIPMAP_APIKEY"),
}

locations = extract_data(url=OPENTRIPMAP_URL,
                         version=VERSION,
                         language=LANGAUGE,
                         endpoint=ENDPOINT,
                         params=request_parameters)

# Store json data in Pandas/Pyspark dataframe
locations_df = store_locations_in_dataframe(locations=locations)

print(locations_df.head())
