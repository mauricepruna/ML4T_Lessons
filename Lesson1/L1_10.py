"""Compute mean volume"""

import pandas as pd

def get_max_close(symbol):
    """Return the maximum closing value for stock indicated symbol.
    
    Note: Data for a stock is stored in a file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) # read in data
    return df['Close'].max() # compute and return max

def test_run_max_close():
    """Function called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print "Max Close"
        print symbol, get_max_close(symbol)

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()  # compute and return mean


def test_run_mean_volume():
    """Function called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print "Mean Volume"
        print symbol, get_mean_volume(symbol)


if __name__ == "__main__":
    test_run_mean_volume()
