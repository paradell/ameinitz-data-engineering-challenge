import sys

sys.path.append("..")

from opentripmap_data.data_extraction import parse_opentripmap_entry


# Test parse_opentripmap_entry
def test_parse_opentripmap_entry_fully_populated():
    entry = {
        "xid": "N3355811093",
        "name": "Hotel Centre",
        "rate": 1,
        "osm": "node/3355811093",
        "wikidata": "Q11682616",
        "kinds": "accomodations,other_hotels",
        "point": {"lon": 2.0446624755859375, "lat": 41.38056945800781},
    }
    expected_result = [
        {
            "xid": "N3355811093",
            "name": "Hotel Centre",
            "rate": 1,
            "osm": "node/3355811093",
            "wikidata": "Q11682616",
            "kinds": "accomodations,other_hotels",
            "longitude": 2.0446624755859375,
            "latitude": 41.38056945800781,
        }
    ]
    assert parse_opentripmap_entry(entry) == expected_result


def test_parse_opentripmap_entry_no_wikidata():
    entry = {
        "xid": "N3355811093",
        "name": "Hotel Centre",
        "rate": 1,
        "osm": "node/3355811093",
        "kinds": "accomodations,other_hotels",
        "point": {"lon": 2.0446624755859375, "lat": 41.38056945800781},
    }
    expected_result = [
        {
            "xid": "N3355811093",
            "name": "Hotel Centre",
            "rate": 1,
            "osm": "node/3355811093",
            "wikidata": None,
            "kinds": "accomodations,other_hotels",
            "longitude": 2.0446624755859375,
            "latitude": 41.38056945800781,
        }
    ]
    assert parse_opentripmap_entry(entry) == expected_result


def test_parse_opentripmap_entry_no_osm():
    entry = {
        "xid": "N3355811093",
        "name": "Hotel Centre",
        "rate": 1,
        "wikidata": "Q11682616",
        "kinds": "accomodations,other_hotels",
        "point": {"lon": 2.0446624755859375, "lat": 41.38056945800781},
    }
    expected_result = [
        {
            "xid": "N3355811093",
            "name": "Hotel Centre",
            "rate": 1,
            "osm": None,
            "wikidata": "Q11682616",
            "kinds": "accomodations,other_hotels",
            "longitude": 2.0446624755859375,
            "latitude": 41.38056945800781,
        }
    ]
    assert parse_opentripmap_entry(entry) == expected_result


def test_parse_opentripmap_entry_no_osm_nor_wikidata():
    entry = {
        "xid": "N3355811093",
        "name": "Hotel Centre",
        "rate": 1,
        "kinds": "accomodations,other_hotels",
        "point": {"lon": 2.0446624755859375, "lat": 41.38056945800781},
    }
    expected_result = [
        {
            "xid": "N3355811093",
            "name": "Hotel Centre",
            "rate": 1,
            "osm": None,
            "wikidata": None,
            "kinds": "accomodations,other_hotels",
            "longitude": 2.0446624755859375,
            "latitude": 41.38056945800781,
        }
    ]
    assert parse_opentripmap_entry(entry) == expected_result
