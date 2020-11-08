from datetime import datetime


class TickersByDate:
    def __init__(self, date: datetime):
        self.date = date
        self.mentioned_tickers = dict()

    def add_tickers(self, tickers: set, message: str) -> 'TickersByDate':
        for ticker in tickers:
            self.mentioned_tickers[ticker] = self.mentioned_tickers.get(ticker, list()) + [message]
        return self

    def get_tickers(self) -> dict:
        return self.mentioned_tickers

    def get_mentioned_tickers(self) -> dict:
        return self.mentioned_tickers

    def __repr__(self):
        return "TickersByDate(" + str(self.date) + " : " + str(self.mentioned_tickers) + ")"

    def __str__(self):
        return self.__repr__()
