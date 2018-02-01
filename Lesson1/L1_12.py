"""Plot High prices for AAPL and IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run_AAPL():
    df = pd.read_csv("data/AAPL.csv")
    print df[['Close','Adj Close']]
    df[['Close','Adj Close']].plot()
    plt.show() #must be called to show the plots

def test_run_IBM():
    df = pd.read_csv("data/IBM.csv")
    print df['High']
    df['High'].plot()
    plt.xlabel('Interval')
    plt.ylabel('High Prices')
    plt.title('Histogram of IBM')
    plt.show()  # must be called to show the plots
if __name__ == "__main__":
    test_run_AAPL()