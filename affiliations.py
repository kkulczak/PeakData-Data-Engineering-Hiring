import pandas as pd

from constants import Countries


def extract_affiliations(affiliations: pd.DataFrame) -> pd.DataFrame:
    exploded = affiliations.dropna().str.strip(' ,.\t\n')
    raw = exploded[exploded.str.len() >= 1].drop_duplicates()
    countries_in_data = set()
    for c in Countries:
        if exploded.str.contains(c).any():
            countries_in_data.add(c)

    splitted = []
    for string in raw[:]:
        found_c = sorted([
            (count, c)
            for c in countries_in_data
            if (count := string.find(c)) > 0
        ])
        if len(found_c) == 0:
            splitted.append(string)
        last_i = 0
        for i, c in found_c:
            splitted.append(string[last_i:i + len(c)])
            last_i = i + len(c)

    splitted_df = pd.Series(splitted).str.strip(' ,.')
    return splitted_df[~splitted_df.str.lower().duplicated()]

