import json
import constants
from data_parser import DataParser
from plot_mentions import plot_mentions
from datetime import datetime
from summarizer import get_summary


def get_logs():
    dp = DataParser(constants.log_file_path)
    mentions_by_ticker = dp.mentions_by_ticker()

    # summarize by user
    clustered_messages = dp.messages_by_user('JohnArtman', start_date=datetime(2018, 6, 1), end_date=datetime(2019, 1, 1))
    summarized_messages = get_summary(clustered_messages, 5)
    print(summarized_messages)

    # need to convert to id
    # plot_mentions(mentions_by_ticker, 'GOOG')
    # pretty(mentions_by_ticker)


def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))


if __name__ == '__main__':
    get_logs()
