from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from data import mission_data, motors_data
from elements import SectionTitle, DataTable
from graphs import MotorGraph


class MotorsList(BoxLayout):

    def __init__(self, **kwargs):
        super(MotorsList, self).__init__(**kwargs)

        self.orientation = 'horizontal'

        self.add_widget(Label(text='Motor 1'))
        self.add_widget(Label(text='Motor 2'))

        self.add_widget(Label(text='Motor 3'))
        self.add_widget(Label(text='Motor 4'))
        self.add_widget(Label(text='Motor 5'))


class MotorsFrame(GridLayout):

    def __init__(self, **kwargs):
        super(MotorsFrame, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(MotorGraph(data=motors_data, x_name='minutes', y_names=['Motor 1', 'Motor 2', 'Motor 3',
                                                                                'Motor 4', 'Motor 5', ]))
        self.add_widget(MotorGraph(data=motors_data, x_name='minutes', y_names=['Motor 1', ]))

        self.add_widget(MotorGraph(data=motors_data, x_name='minutes', y_names=['Motor 2', ]))
        self.add_widget(MotorGraph(data=motors_data, x_name='minutes', y_names=['Motor 3', ]))
        self.add_widget(MotorGraph(data=motors_data, x_name='minutes', y_names=['Motor 4', ]))
        self.add_widget(MotorGraph(data=motors_data, x_name='minutes', y_names=['Motor 5', ]))