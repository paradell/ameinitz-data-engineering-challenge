# Extract 2500 entries from Open Trip Map
import os

import requests

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
r = requests.get(
    f"{OPENTRIPMAP_URL}/{VERSION}/{LANGAUGE}/{ENDPOINT}", params=request_parameters
)

# Validate the data extracted from Open Trip Map
print(f"{r.status_code}") if r.status_code == 200 else print(
    f"Something went wrong, " f"API returned {r.status_code} response."
)

print(f"{len(r.json())} rows entries extracted correctly.") if len(
    r.json()
) == LIMIT else print(
    f"Something went wrong"
    f", expected {LIMIT} "
    f"entries but got "
    f"{len(r.json())}."
)
