import matplotlib.pyplot as plt
import json


def plot_mentions(data: dict, ticker: str):
    x_data = []
    y_data = []
    for date in data:
        x_data.append(date)
        y_data.append(len(data[date].get_mentioned_tickers()))

    plt.ylabel('Date')
    plt.plot(x_data, y_data, 'ro')
    plt.show()
