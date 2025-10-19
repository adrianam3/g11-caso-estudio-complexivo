import pandas as pd
import os

# ruta absoluta de la carpeta donde esta el script (.../scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ruta absoluta del archivo data.csv (.../data/data.csv)
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", 'flights.csv')     

def cargar_datos(path):
    print(f"Cargando datos desde: {path}..")
    
    try:
        flights = pd.read_csv(path)
        print("Datos cargados correctamente !!!.")
        return flights      #flights= dataframe
    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en la ruta especificada: {path}")
        print("Verifique que el archivo exista y la ruta sea correcta carpeta 'data'.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inseperado: {e}")
        return None
    

 # ¿este archivo se está ejcutando directamente por el usuario o esta siendo importado por otro script ?    
if __name__ == "__main__":
    # indica donde esta el script actual
    # print(f"El script se está ejecutando desde: {os.path.abspath(__file__)}")
    print(f"El script se está ejecutando desde: {DATA_PATH}")    
    #llamar a la función de arriba para cargar el csv cargar_datos
    dataframe_vuelos = cargar_datos(DATA_PATH)
  
    if dataframe_vuelos is not None:
        print("\n---Primeras 5 filas--")
        print(dataframe_vuelos.head())
        print("\n---Información del dataframe--")
        dataframe_vuelos.info(show_counts=True)
        
         