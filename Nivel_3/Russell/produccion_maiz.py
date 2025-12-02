import pandas as pd
import numpy as np

def limpiar_datos_produccion(nombre_archivo: str) -> pd.DataFrame:
    """
    Carga un archivo CSV, elimina filas con valores nulos y elimina
    filas completamente duplicadas.

    Args:
        nombre_archivo (str): Nombre del archivo CSV a cargar.

    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    print(f"--- 📂 Cargando archivo: {nombre_archivo} ---")
    try:
        # Cargar el archivo CSV
        df = pd.read_csv(nombre_archivo)
    except FileNotFoundError:
        print(f"ERROR: El archivo '{nombre_archivo}' no se encontró.")
        return pd.DataFrame() # Retorna un DataFrame vacío si hay error

    # 1. Limpieza de Duplicados
    
    # Identificar duplicados ANTES de eliminarlos
    duplicados = df[df.duplicated(keep='first')]
    print(f"\n--- 📝 Resumen antes de la limpieza ---")
    print(f"Filas totales (incluyendo duplicados y nulos): {len(df)}")
    print(f"Filas completamente duplicadas encontradas: {len(duplicados)}")

    # Eliminar filas duplicadas, manteniendo la primera aparición
    df_sin_duplicados = df.drop_duplicates(keep='first')
    
    # 2. Limpieza de Valores Nulos (NaN)
    
    # Identificar filas con valores nulos en la columna 'Producción (kg)' ANTES de eliminarlas
    nulos_detectados = df_sin_duplicados[df_sin_duplicados['Producción (kg)'].isna()]
    print(f"Filas con valores nulos detectadas: {len(nulos_detectados)}")
    
    # Eliminar filas con CUALQUIER valor nulo (aunque solo tenemos en 'Producción (kg)')
    df_limpio = df_sin_duplicados.dropna(how='any')

    print(f"\n--- ✅ Limpieza Finalizada ---")
    print(f"Total de filas limpias: {len(df_limpio)}")
    print(f"Filas eliminadas en total: {len(df) - len(df_limpio)}")
    
    print("\n--- 🧹 Filas Duplicadas Eliminadas (Ejemplo) ---")
    if not duplicados.empty:
        print(duplicados)
    else:
        print("No se eliminaron filas duplicadas.")

    print("\n--- 🗑️ Filas con Valores Nulos Eliminadas (Ejemplo) ---")
    if not nulos_detectados.empty:
        print(nulos_detectados)
    else:
        print("No se eliminaron filas con valores nulos.")
        
    return df_limpio

# --- Ejecución de la función ---

# El nombre del archivo que has proporcionado
nombre_del_archivo = "produccion_maiz.csv"

# Llamar a la función
df_limpio = limpiar_datos_produccion(nombre_del_archivo)

# Mostrar las primeras filas del DataFrame limpio
if not df_limpio.empty:
    print("\n--- ✨ DataFrame Limpio (Primeras 5 filas) ---")
    print(df_limpio.head())