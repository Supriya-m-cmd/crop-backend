annual_rainfall = {

    "Hubli": 838,

    "Dharwad": 838,

    "Belagavi": 1250,

    "Gadag": 730,

    "Haveri": 792,

    "Vijayapura": 578,

    "Bagalkot": 562,

    "Bengaluru": 970,

    "Mysuru": 782,

    "Ballari": 608
}


def get_annual_rainfall(
    district
):

    return annual_rainfall.get(
        district,
        800
    )