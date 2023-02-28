import yfinance as yf
import talib

# Define el ticker y el rango de fechas
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2021-12-31"

# Obtén los datos de precios de cierre del ticker usando yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Extrae los precios de cierre en una lista
prices = data["Adj Close"].tolist()

# Encuentra los patrones de Hombro-Cabeza-Hombro y Hombro-Cabeza-Hombro Invertido usando talib
sma = talib.SMA(prices, timeperiod=20) # calcular el promedio móvil simple de 20 días
patterns = talib.CDLSHOULDERHEADSHOULDER(prices) + talib.CDLINVERTEDSHOULDERHEADSHOULDER(prices)

# Imprime los resultados
print(f"Patrones encontrados en el ticker {ticker}:")
for i in range(len(patterns)):
    if patterns[i] != 0:
        print(f"Patrón encontrado en el día {i}: {talib.get_function_name(patterns[i])}")
