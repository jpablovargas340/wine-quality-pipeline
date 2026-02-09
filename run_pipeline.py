from __future__ import annotations
from pathlib import Path
import pandas as pd

from src.cleaning import rename_columns, drop_duplicates, basic_filters

RAW_PATH = Path("data/raw/winequality-red.csv")
OUT_PATH = Path("data/processed/winequality_red_clean.csv")

def main() -> None:
    if not RAW_PATH.exists():
        raise FileNotFoundError(f"Dataset no encontrado: {RAW_PATH.resolve()}")

    df: pd.DataFrame = pd.read_csv(RAW_PATH, sep=";")
    df = rename_columns(df)
    df = drop_duplicates(df)
    df = basic_filters(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print("\nPreview:")
    print(df.head())
    print("\nGuardado en:", OUT_PATH)

if __name__ == "__main__":
    main()
