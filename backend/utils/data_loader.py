import yfinance as yf
import pandas as pd
import numpy as np

def descargar_datos(tickers, start, end):
    """
    Descarga datos históricos ajustados desde Yahoo Finance.
    """
    datos = yf.download(tickers, start=start, end=end)['Adj Close']
    return datos

def calcular_rendimientos(datos):
    """
    Calcula los rendimientos logarítmicos de los activos.
    """
    return np.log(datos / datos.shift(1))
