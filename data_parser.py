import json
from get_all_tickers import get_tickers as gt
from tickers_by_date import TickersByDate
from datetime import datetime
import constants


class DataParser:
    def __init__(self, filepath: str):
        self.message = self.get_messages(filepath)

    def mentions_by_ticker(self) -> dict:
        ticker_mentions = {}
        tickers = set(gt.get_tickers())
        for message in self.message:
            # split message to look for tickers
            message_by_parts = message["content"].split(" ")
            # in_message is mentioned tickers
            in_message = set(message_by_parts).intersection(tickers)
            date = datetime.strptime(message["timestamp"].split('T')[0], '%Y-%m-%d')
            # map by date, messages
            ticker_mentions[date] = ticker_mentions.get(date, TickersByDate(date)).add_tickers(in_message, message)
        return ticker_mentions


    @staticmethod
    def get_messages(filepath: str) -> json:
        with open(filepath) as json_file:
            data = json.load(json_file)
            return data["messages"]


    # {
    #   "id": "516598346916429834",
    #   "type": "Default",
    #   "timestamp": "2018-11-26T12:57:23.838+00:00",
    #   "timestampEdited": null,
    #   "callEndedTimestamp": null,
    #   "isPinned": false,
    #   "content": "Wow",
    #   "author": {
    #     "id": "244185245698621440",
    #     "name": "L\u00FCshB\u00F5i",
    #     "discriminator": "9930",
    #     "isBot": false,
    #     "avatarUrl": "https://cdn.discordapp.com/avatars/244185245698621440/f28cc41763f214c8328d1ad805a3dbc5.png"
    #   },
    #   "attachments": [],
    #   "embeds": [],
    #   "reactions": [],
    #   "mentions": []
    # }