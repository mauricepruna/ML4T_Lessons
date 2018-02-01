"""Fill missing values"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def compute_daily_returns(df):
    """Compute and return the daily return values"""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df_final = pd.DataFrame(index=dates)
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")

    for symbol in symbols:
        file_path = symbol_to_path(symbol)
        df_temp = pd.read_csv(file_path, parse_dates=True, index_col="Date",
            usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df_final = df_final.join(df_temp)
        if symbol == "SPY":  # drop dates SPY did not trade
            df_final = df_final.dropna(subset=["SPY"])

    return df_final


def plot_data(df_data, title='Stock Data', ylabel='Price'):
    """Plot stock data with appropriate axis labels."""
    ax = df_data.plot(title = title)
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)

    plt.show()


def test_run():
    """Function called by Test Run."""
    # Read data
    # symbol_list = ["JAVA", "FAKE1", "FAKE2"]  # list of symbols
    symbol_list = ["SPY"]
    start_date = "2009-01-01"
    end_date = "2012-12-31"
    dates = pd.date_range(start_date, end_date)  # date range as index
    df_data = get_data(symbol_list, dates)  # get data for each symbol
    #plot_data(df_data)
    daily_returns  = compute_daily_returns(df_data)
    # Plot
    #plot_data(daily_returns, title="Daily return", ylabel = "Daily returns")


    daily_returns.hist(bins=20)

    #Get mean and standard deviation
    mean = daily_returns['SPY'].mean()
    print "mean", mean
    std = daily_returns['SPY'].std()
    print "std=", std
    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
    plt.axvline(std,color='r',linestyle='dashed',linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()

    print daily_returns.kurtosis()

if __name__ == "__main__":
    test_run()
