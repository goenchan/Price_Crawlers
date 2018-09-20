from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='HO5YUWIBEZJF7BRQ', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='compact')
print(data.head())