"""
Script para preprocesar datos de valoración de jugadores alrededor de los años.
"""

import numpy as np
import pandas as pd
import os


def get_year_and_market_value_from_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Obtiene el año y valor de mercado únicamente a partir
    del DataFrame.
    """
    # Obtengo el año
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year

    # Me quedo solo con las columnas que me interesan
    df = df[["year", "market_value_in_eur"]].copy()
    df = df.dropna()
    return df


def get_log_mean_market_value_from_years(df: pd.DataFrame) -> pd.DataFrame:
    """
    Obtiene el valor de mercado medio por año en escala logarítmica.
    """
    df_grouped = df.groupby("year")["market_value_in_eur"].mean().reset_index()
    df_grouped["log_market_value_in_eur"] = np.log10(df_grouped["market_value_in_eur"])
    return df_grouped[["year", "log_market_value_in_eur"]]


if __name__ == "__main__":
    ruta_archivo = os.path.join("ejercicios", "data", "raw", "player_valuations.csv")
    df_player_valuations = pd.read_csv(ruta_archivo)

    df = get_year_and_market_value_from_df(df_player_valuations)
    df_mean = get_log_mean_market_value_from_years(df)

    ruta_guardado = os.path.join(
        "ejercicios", "data", "processed", "player_valuations_log_mean.csv"
    )
    df_mean.to_csv(ruta_guardado, index=False)
