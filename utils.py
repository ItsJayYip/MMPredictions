'''
    utils.py

    Copyright (c) 2025, Reid Simmons, Carnegie Mellon University
      This software is distributed under the terms of the
      Simplified BSD License (see ipc/LICENSE.TXT)
'''
from pathlib import Path

import pandas as pd


def read_data(file_name, which='M'):
    subdir = 'mens' if which == 'M' else 'womens'
    data_path = Path('data') / subdir / f'{which}{file_name}.csv'
    return pd.read_csv(data_path)

def read_predictions(whom, which='M'):
    return pd.read_csv('submissions/%sNCAATourneyPredictions - %s.csv'
                       %(which, whom))