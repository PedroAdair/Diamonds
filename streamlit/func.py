import pandas as pd


def load_data():
    return pd.read_csv('streamlit\diamonds_clean.csv', index_col=0)

def mensaje():
    msg = """Se realizo un trabajo sobre una coleccion proporcionada, la cual contiene un total de 53,930 registros. 
    De los cuales se encontro que 2,962 tenian al menos un valor faltante. Se realizo una investigacion y se encontro una posible relación."""
    return msg


def datosFaltantes():
    data = {
    "Caso": ["I", "II", "III", "IV", "V", "VI", "VII", "Total"],
    "x": ["Si", "Si", "No", "No", "No", "Si", "No", ""],
    "y": ["Si", "No", "Si", "No", "Si", "No", "No", ""],
    "depth": ["No", "Si", "Si", "Si", "No", "No", "No", ""],
    "Cantidad": [1872, 0, 0, 0, 505, 0, 585, 2962],
    "%": [63.20, 0, 0, 0, 17.05, 0, 19.75, 100]
    }

    df = pd.DataFrame(data)
    df.set_index('Caso', inplace=True)
    return df
