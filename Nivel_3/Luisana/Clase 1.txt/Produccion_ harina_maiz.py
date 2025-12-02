import pandas as pd
from io import StringIO

def limpiar_datos_produccion(nombre_archivo: str, contenido_csv: str) -> pd.DataFrame:
    """
    Carga un conjunto de datos CSV, elimina filas con valores nulos y filas duplicadas.

    Args:
        nombre_archivo (str): El nombre del archivo CSV (solo se usa para referencia).
        contenido_csv (str): El contenido del archivo CSV en formato de cadena de texto.

    Returns:
        pd.DataFrame: Un DataFrame de Pandas limpio.
    """
    print(f"Iniciando la limpieza del conjunto de datos: {nombre_archivo}...")

    # 1. Cargar los datos desde la cadena de texto (simulando la lectura del archivo)
    try:
        # Usamos StringIO para tratar la cadena de texto como un archivo
        data_io = StringIO(contenido_csv)
        df = pd.read_csv(data_io)
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return pd.DataFrame() # Retorna un DataFrame vacío en caso de error

    print(f"Dimensiones originales del DataFrame: {df.shape}")

    # --- 2. Eliminar filas con valores nulos (missing values) ---
    # La columna 'Producción (kilos)' tiene un valor nulo para Noviembre de 2020
    df_limpio_nulos = df.dropna()
    filas_eliminadas_nulos = df.shape[0] - df_limpio_nulos.shape[0]

    print(f"Filas con valores nulos eliminadas: {filas_eliminadas_nulos}")
    print(f"Dimensiones después de eliminar nulos: {df_limpio_nulos.shape}")

    # --- 3. Eliminar filas duplicadas ---
    # df.drop_duplicates() mantiene la primera ocurrencia y elimina las siguientes
    df_limpio_final = df_limpio_nulos.drop_duplicates()
    filas_eliminadas_duplicadas = df_limpio_nulos.shape[0] - df_limpio_final.shape[0]

    print(f"Filas duplicadas eliminadas: {filas_eliminadas_duplicadas}")
    print(f"Dimensiones finales del DataFrame: {df_limpio_final.shape}")

    return df_limpio_final

# --- Uso de la Función ---

# Contenido del archivo proporcionado (simulando la lectura)
contenido_archivo = """Año,Mes,Producción (kilos)
2020,Enero,10000
2020,Febrero,12000
2020,Marzo,11000
2020,Abril,15000
2020,Mayo,14000
2020,Junio,16000
2020,Julio,17000
2020,Agosto,18000
2020,Septiembre,19000
2020,Octubre,20000
2020,Noviembre,
2020,Diciembre,21000
2021,Enero,22000
2021,Febrero,23000
2021,Marzo,24000
2021,Abril,25000
2021,Mayo,26000
2021,Junio,27000
2021,Julio,28000
2021,Agosto,29000
2021,Septiembre,30000
2021,Octubre,31000
2021,Noviembre,31000
2021,Diciembre,32000
2022,Enero,33000
2022,Febrero,34000
2022,Marzo,35000
2022,Abril,36000
2022,Mayo,37000
2022,Junio,38000
2022,Julio,39000
2022,Agosto,40000
2022,Septiembre,41000
2022,Octubre,42000
2022,Noviembre,43000
2022,Diciembre,44000
2023,Enero,45000
2023,Febrero,46000
2023,Marzo,47000
2023,Abril,48000
2023,Mayo,49000
2023,Junio,50000
2023,Julio,51000
2023,Agosto,52000
2023,Septiembre,53000
2023,Octubre,54000
2023,Noviembre,54000
2023,Diciembre,55000
2024,Enero,56000
2024,Febrero,57000
2024,Marzo,58000
2024,Abril,59000
2024,Mayo,60000
2024,Junio,61000
2024,Julio,62000
2024,Agosto,63000
2024,Septiembre,64000
2024,Octubre,65000
2024,Noviembre,65000
2024,Diciembre,66000
2025,Enero,67000
2025,Febrero,68000
2025,Marzo,69000
2025,Abril,70000
2025,Mayo,71000
2025,Junio,72000
2025,Julio,73000
2025,Agosto,74000
2025,Septiembre,75000
2025,Octubre,76000
2025,Noviembre,76000
2025,Diciembre,77000
""" # 

df_limpio = limpiar_datos_produccion("Producción_ Harina de Maíz (2020-2025)", contenido_archivo)

# Muestra las filas limpias (quitando la fila 2020, Noviembre)
print("\n--- Primeras filas del DataFrame limpio ---")
print(df_limpio.head(15))