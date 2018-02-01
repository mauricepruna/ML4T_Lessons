"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        curr_csv = symbol_to_path(symbol)
        df_temp = pd.read_csv(curr_csv, index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])

    return df


def plot_data(df, xlabel, ylabel, title="Stock Prices"):
    '''Plot sotck prices'''
    ax = df.plot(title = title)
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel)

    plt.show()  # must be called to show the plots


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    # Slice by row range (dates) using Dataframe.ix[] selector
    # print df.ix['2010-01-01': '2010-01-31'] #January

    # Slice
    # print "==a single label selects a single column=="
    # print df[['GOOG']] # a single label selects a single column
    # print "==a list of labels selects multiple columns =="
    # print df[['IBM','GLD']] # a list of labels selects multiple columns

    # Slice by row and column
    print df

    # df = df / df.ix[0]
    # for date in df.index:
    #     for s in symbols:
    #         df[date,s] = df[date,s]/df[0,s]
    # df.ix['2010-03-10': '2010-03-15', ['SPY', 'IBM']].plot()

    plot_data(df, 'Date', 'Price')


if __name__ == "__main__":
    test_run()
