import logging
import sys
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(HERE)

from benchmark_data import *
import backup_pickle


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    backup_pickle.save_session()
