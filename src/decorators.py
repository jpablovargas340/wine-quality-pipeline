from __future__ import annotations
from functools import wraps
from typing import Callable
import pandas as pd

def log_step(func: Callable[[pd.DataFrame], pd.DataFrame]) -> Callable[[pd.DataFrame], pd.DataFrame]:
    @wraps(func)
    def wrapper(df: pd.DataFrame) -> pd.DataFrame:
        print(f"[STEP] {func.__name__} | in={df.shape}")
        out = func(df)
        print(f"[DONE] {func.__name__} | out={out.shape}")
        return out
    return wrapper
