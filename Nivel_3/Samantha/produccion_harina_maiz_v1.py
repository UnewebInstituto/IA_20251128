import pandas as pd
import numpy as np
from typing import Optional

def limpiar_datos_produccion(archivo_entrada="produccion_harina_maiz.csv", archivo_salida="produccion_harina_maiz_limpio.csv"):
    """
    Limpia el conjunto de datos de producción de harina de maíz:
    - Elimina filas con valores nulos.
    - Elimina duplicados por Año y Mes (manteniendo el primero).
    
    Parámetros:
    archivo_entrada (str): Ruta del archivo CSV original.
    archivo_salida (str): Ruta del archivo CSV limpio a generar.
    """
    # Leer el CSV
    df = pd.read_csv(archivo_entrada)
    
    print(f"Filas originales: {len(df)}")
    
    # Mostrar información inicial
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    
    print("\nDuplicados exactos:")
    print(df.duplicated().sum())
    
    # 1. Eliminar filas con cualquier valor nulo
    df = df.dropna()
    print(f"\nFilas tras eliminar nulos: {len(df)}")
    
    # 2. Eliminar duplicados por combinación de Año y Mes
    # Convertir Año y Mes a tipos correctos por si acaso
    df['Año'] = df['Año'].astype(int)
    df['Mes'] = df['Mes'].astype(str)
    
    # Eliminar duplicados manteniendo el primero
    df = df.drop_duplicates(subset=['Año', 'Mes'], keep='first')
    print(f"Filas tras eliminar duplicados por Año-Mes: {len(df)}")
    
    # Opcional: ordenar por Año y Mes
    meses_orden = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                   'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    df['Mes_orden'] = df['Mes'].map({mes: i for i, mes in enumerate(meses_orden)})
    df = df.sort_values(['Año', 'Mes_orden']).drop('Mes_orden', axis=1)
    
    # Guardar el archivo limpio
    df.to_csv(archivo_salida, index=False)
    print(f"\nDatos limpios guardados en: {archivo_salida}")
    
    return df

# Ejecutar la función
if __name__ == "__main__":
    df_limpio = limpiar_datos_produccion()
    print("\nPrimeras filas del dataset limpio:")
    print(df_limpio.head(12))