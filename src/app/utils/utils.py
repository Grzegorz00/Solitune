import pandas as pd

def get_casts(xs: pd.Series) -> dict[int,list[str]]:
    return dict(xs.str.split("|"))