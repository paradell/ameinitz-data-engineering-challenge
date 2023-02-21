import pandas as pd
import requests


def extract_data(url, version, language, endpoint, params):
    r = requests.get(f"{url}/{version}/{language}/{endpoint}",
                     params=params)

    # Validate the data extracted from Open Trip Map
    print(f"{r.status_code}") if r.status_code == 200 else print(
        f"Something went wrong, " f"API returned {r.status_code} response."
    )

    print(f"{len(r.json())} rows entries extracted correctly.") if len(r.json()) == params['limit'] else print(
        f"Something went wrong, expected {params['limit']} entries but got {len(r.json())}."
    )

    return r.json()


def parse_opentripmap_entry(entry):
    # Format the entry to be compatible with the Pandas dataframe used for this challenge
    try:
        osm = entry['osm']
    except KeyError:
        osm = None

    try:
        wikidata = entry['wikidata']
    except KeyError:
        wikidata = None

    return [{
        'xid': entry['xid'],
        'name': entry['name'],
        'rate': entry['rate'],
        'osm': osm,
        'wikidata': wikidata,
        'kinds': entry['kinds'],
        'longitude': entry['point']['lon'],
        'latitude': entry['point']['lat']
    }]


def store_locations_in_dataframe(locations):
    # Create Dataframe
    df = pd.DataFrame(
        columns=["xid", "name", "rate", "osm", "wikidata", "kinds", "longitude", "latitude"]
    )

    # Append all entries
    for location in locations:
        df = pd.concat([df, pd.DataFrame(parse_opentripmap_entry(location))],
                       axis=0,
                       ignore_index=True)
    return df
