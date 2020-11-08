import json
import constants
from data_parser import DataParser
from plot_mentions import plot_mentions


def get_logs():
    dp = DataParser(constants.log_file_path)
    mentions_by_ticker = dp.mentions_by_ticker()
    plot_mentions(mentions_by_ticker, 'GOOG')
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
