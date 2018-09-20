# import needed libraries
import quandl
import pandas as pd

# add quandl API key for unrestricted
quandl.ApiConfig.api_key = 'BosxjhVB3TpcG-BDzGRr'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call
data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT'],
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
                        date = { 'gte': '2018-03-24', 'lte': '2018-09-01' },
                        paginate=True)

# create a new dataframe with 'date' column as index
new = data.set_index('date')

# use pandas pivot function to sort adj_close by tickers
clean_data = new.pivot(columns='ticker')
print(data)