import pandas as pd


class ChData(object):
    def __init__(self):
        colnames = ['aa', 'mm', 'gg', 'hh', 'mm', 'ss', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9',
                    'ch10', 'ch11', 'ch12', ]

        ch_data = pd.read_csv('./ch1-12.csv', sep=';', error_bad_lines=False, names=colnames)

        self.data = ch_data

        f_data = pd.read_csv('./f1-f4.csv', sep=';', error_bad_lines=False)
        mod_data = pd.read_csv('./mod.csv', sep=';', error_bad_lines=False)

data = ChData()