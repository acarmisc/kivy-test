from kivy.uix.boxlayout import BoxLayout

from data import mission_data

from elements import SectionTitle, DataTable


class MissionLog(BoxLayout):

    def __init__(self, **kwargs):
        super(MissionLog, self).__init__(**kwargs)

        self.orientation = 'vertical'

        data_table = DataTable(data=mission_data)
        self.add_widget(data_table)
