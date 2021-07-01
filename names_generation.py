import pandas as pd


def extract_names(authors: pd.DataFrame) -> pd.DataFrame:
    def f(x):
        x = x.strip('[]\"\'')
        return x.split(',')

    extracted_authors = authors.dropna().apply(f).explode().str.strip(' \'\"').drop_duplicates()

    first_name = extracted_authors.apply(lambda x: x.split(' ')[0])
    last_name = extracted_authors.apply(lambda x: x.split(' ')[-1])

    final = pd.DataFrame(dict(first_name=first_name, last_name=last_name)).reset_index(drop=True)

    long = final[final.first_name.str.len() >= 2].drop_duplicates()
    full = long[long.first_name.str.contains('^[a-zA-Z]+$')]
    return full.reset_index(drop=True)
