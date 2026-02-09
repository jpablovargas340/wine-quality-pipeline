from __future__ import annotations
import pandas as pd
from .decorators import log_step

@log_step
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns=lambda c: c.strip().replace(" ", "_"))

@log_step
def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

@log_step
def basic_filters(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["quality"].between(3, 8)]
    df = df[df["alcohol"].between(8, 15)]
    df = df[df["pH"].between(2.8, 4.2)]
    return df