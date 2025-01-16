"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    # Importar librerias
    import pandas as pd
    import os

    # Leer archivo
    df = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';', index_col=0)

    # Corregir errores en la columna "sexo"
    df['sexo'] = df['sexo'].str.lower()

    # Corregir errores en la columna "tipo_de_emprendimiento"
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().str.strip()

    # Corregir errores en la columna "idea_negocio"
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("-", "_").str.replace(" ", "_").str.strip()

    # Corregir errores en la columna "barrio"
    df['barrio'] = df['barrio'].str.lower().str.replace(" ", "_").str.replace("-", "_").str.strip()

    # Corregir errores en la columna "estrato"
    df['estrato'] = df['estrato'].astype(int)

    # Corregir errores en la columna "comuna_ciudadano"
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    # Corregir errores en la columna "fecha_de_beneficio"
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    # Corregir errores en la columna "monto_del_credito"
    df['monto_del_credito'] = df['monto_del_credito'].str.strip().str.replace("$", '').str.replace(",", "").str.replace(".00", "").astype(int)

    # Corregir errores en la columna "línea_credito"
    df['línea_credito'] = df["línea_credito"].str.lower().str.replace(" ", "_").str.replace("-", "_").str.strip()

    # Eliminar registros duplicados
    df = df.drop_duplicates()

    # Eliminar registros con datos faltantes
    df = df.dropna()

    # Guardar archivo limpio con librería os
    if not os.path.exists('files/output'):
        os.makedirs('files/output')
    df.to_csv('files/output/solicitudes_de_credito.csv', sep=';', index=False)

pregunta_01()