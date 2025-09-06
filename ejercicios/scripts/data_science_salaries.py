"""
Script para preprocesar datos de salarios en ciencia de datos 2020-2024.
"""

import numpy as np
import pandas as pd
import os


def get_relevant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Obtiene las columnas relevantes del DataFrame.
    """
    columnas_relevantes = [
        "work_year",
        "experience_level",
        "employee_residence",
        "salary_in_usd",
    ]
    df = df[columnas_relevantes].copy()
    df = df.dropna()
    return df


def filter_year_and_drop_column(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """
    Filtra el DataFrame para quedarse solo con el año 2024 y elimina la columna work_year.
    """
    df = df[df["work_year"] == year].copy()
    df = df.drop(columns=["work_year"])
    return df


def scale_to_log10(df: pd.DataFrame) -> pd.DataFrame:
    """
    Escala la columna salary_in_usd a escala logarítmica base 10.
    """
    df["log_salary_in_usd"] = np.log10(df["salary_in_usd"])
    df = df.drop(columns=["salary_in_usd"])
    return df


if __name__ == "__main__":
    ruta_archivo = os.path.join(
        "ejercicios", "data", "raw", "DataScience_salaries_2024.csv"
    )
    df_salaries = pd.read_csv(ruta_archivo)

    df_salaries = get_relevant_columns(df_salaries)

    df_salaries_2024 = filter_year_and_drop_column(df_salaries, year=2024)

    df_salaries_2024 = scale_to_log10(df_salaries_2024)

    ruta_guardado = os.path.join(
        "ejercicios", "data", "processed", "data_science_salaries_2024.csv"
    )
    df_salaries_2024.to_csv(ruta_guardado, index=False)
