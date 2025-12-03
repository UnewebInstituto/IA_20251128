import pandas as pd
import numpy as np
from typing import Optional

def limpiar_datos_produccion(nombre_archivo: str) -> Optional[pd.DataFrame]:
    """
    Carga un archivo CSV, elimina valores nulos y filas duplicadas.

    Args:
        nombre_archivo (str): El nombre del archivo CSV a cargar.

    Returns:
        Optional[pd.DataFrame]: Un DataFrame de Pandas limpio, o None si hay un error al cargar el archivo.
    """
    try:
        # 1. Cargar el archivo CSV en un DataFrame de Pandas
        df = pd.read_csv(nombre_archivo)
        print(f"✅ Archivo '{nombre_archivo}' cargado exitosamente.")
        print(f"Filas originales: {len(df)}")
        
        # --- Limpieza de Datos ---
        
        # 2. Eliminar filas con cualquier valor nulo (NaN)
        # El método dropna() elimina filas o columnas que contienen valores faltantes.
        df_limpio_nulos = df.dropna()
        filas_eliminadas_nulos = len(df) - len(df_limpio_nulos)
        print(f"🗑️ Filas eliminadas por valores nulos: {filas_eliminadas_nulos}")
        
        # 3. Eliminar filas duplicadas
        # El método drop_duplicates() elimina las filas donde todas las columnas son idénticas.
        df_final = df_limpio_nulos.drop_duplicates()
        filas_eliminadas_duplicadas = len(df_limpio_nulos) - len(df_final)
        print(f"🗑️ Filas eliminadas por ser duplicados exactos: {filas_eliminadas_duplicadas}")
        
        print(f"\n📊 Total de filas limpias: {len(df_final)}")
        return df_final
        
    except FileNotFoundError:
        print(f"❌ ERROR: El archivo '{nombre_archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")
        return None

# --- Ejemplo de Uso ---

# NOTA: Asumiendo que el archivo 'produccion_harina_maiz.csv' está en la misma carpeta.
nombre_del_archivo = "produccion_harina_maiz.csv"
datos_limpios = limpiar_datos_produccion(nombre_del_archivo)

# Mostrar las primeras filas del DataFrame limpio (si se cargó con éxito)
if datos_limpios is not None:
    print("\n--- Primeras filas del DataFrame Limpio ---")
    print(datos_limpios.head())