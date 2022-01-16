import pandas as pd


data = pd.DataFrame()
mission_data = pd.read_csv('mod.csv')
motors_data = pd.read_csv('f1-f4.csv')
magnetometer_data = pd.read_csv('ch1-12.csv', delimiter=';')
