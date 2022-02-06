import pandas as pd


data = pd.DataFrame()
mission_data = pd.read_csv('datafiles/mod.csv')
motors_data = pd.read_csv('datafiles/f1-f4.csv')
magnetometer_data = pd.read_csv('datafiles/ch1-12.csv', delimiter=';')
