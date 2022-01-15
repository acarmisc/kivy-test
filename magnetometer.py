from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from data import mission_data, motors_data, magnetometer_data
from elements import SectionTitle, DataTable, InfoRow
from graphs import MotorGraph, MagnetometerGraph


class MagnetometerFrame(GridLayout):

    def __init__(self, **kwargs):
        super(MagnetometerFrame, self).__init__(**kwargs)

        self.cols = 1

        sensors = InfoRow(label='Sensors no:', value='12')
        sensors.size_hint_y = 0.1

        self.add_widget(sensors)
        self.add_widget(MagnetometerGraph(data=magnetometer_data, x_name='seconds',
                                          y_names=['mod F1', 'mod F2', 'mod F3', 'mod F4'],
                                          ymin=65373063, ymax=5000000))

        self.add_widget(MagnetometerGraph(data=magnetometer_data, x_name='seconds',
                                          y_names=['D(F2-F1)', 'D(F3-F1)', 'D(F4-F1)'],
                                          ymin=-10000000, ymax=5000000))
