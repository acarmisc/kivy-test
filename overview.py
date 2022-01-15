from kivy.uix.boxlayout import BoxLayout

from elements import SectionTitle, InfoRow
from graphs import Modes


class OverviewFrame(BoxLayout):

    def __init__(self, **kwargs):
        super(OverviewFrame, self).__init__(**kwargs)

        self.orientation = 'vertical'

        overview_title = SectionTitle(local_title='Abstract')
        overview_title.height = 30

        self.add_widget(overview_title)
        self.add_widget(InfoRow(label='Mission date', value='02/02/2019'))
        self.add_widget(InfoRow(label='Start time', value='09:03:02'))
        self.add_widget(InfoRow(label='End Time', value='09:37:02'))
        self.add_widget(InfoRow(label='Total Duration', value='37 min'))
        self.add_widget(InfoRow(label='Mode', value='AUV/ROV'))

        modality_title = SectionTitle(local_title='Modes')
        modality_title.height = 30

        self.add_widget(modality_title)
        self.add_widget(Modes())
