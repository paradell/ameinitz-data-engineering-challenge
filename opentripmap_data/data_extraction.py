# Extract 2500 entries from Open Trip Map
import os

import pandas as pd
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


def extract_data(url, version, language, endpoint, params):
    r = requests.get(f"{url}/{version}/{language}/{endpoint}", params=params)

    # Validate the data extracted from Open Trip Map
    print(f"{r.status_code}") if r.status_code == 200 else print(
        f"Something went wrong, " f"API returned {r.status_code} response."
    )

    print(f"{len(r.json())} rows entries extracted correctly.") if len(
        r.json()
    ) == params["limit"] else print(
        f"Something went wrong, expected {params['limit']} entries but got {len(r.json())}."
    )

    return r.json()


def parse_opentripmap_entry(entry):
    # Format the entry to be compatible with the Pandas dataframe used for this challenge
    try:
        osm = entry["osm"]
    except KeyError:
        osm = None

    try:
        wikidata = entry["wikidata"]
    except KeyError:
        wikidata = None

    return [
        {
            "xid": entry["xid"],
            "name": entry["name"],
            "rate": entry["rate"],
            "osm": osm,
            "wikidata": wikidata,
            "kinds": entry["kinds"],
            "longitude": entry["point"]["lon"],
            "latitude": entry["point"]["lat"],
        }
    ]


def store_locations_in_dataframe(locations):
    # Create Dataframe
    df = pd.DataFrame(
        columns=[
            "xid",
            "name",
            "rate",
            "osm",
            "wikidata",
            "kinds",
            "longitude",
            "latitude",
        ]
    )

    # Append all entries
    for location in locations:
        df = pd.concat(
            [df, pd.DataFrame(parse_opentripmap_entry(location))],
            axis=0,
            ignore_index=True,
        )
    return df


def extract_data_from_opentripmap_to_df(
    url=OPENTRIPMAP_URL,
    version=VERSION,
    language=LANGAUGE,
    endpoint=ENDPOINT,
    params=request_parameters,
):
    locations = extract_data(
        url=url, version=version, language=language, endpoint=endpoint, params=params
    )

    # Store json data in Pandas/Pyspark dataframe
    return store_locations_in_dataframe(locations=locations)
