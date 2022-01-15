from kivy.uix.boxlayout import BoxLayout
from kivy.uix.splitter import Splitter

from elements import SectionTitle, InfoRow


class SensorsFrame(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(SensorsFrame, self).__init__(**kwargs)

        self.orientation = 'vertical'

        overview_title = SectionTitle(local_title='Available Sensors')

        overview_title.height = 30

        self.add_widget(overview_title)
        self.add_widget(InfoRow(label='Camera', value='YES'))
        self.add_widget(InfoRow(label='GPS', value='YES'))
        self.add_widget(InfoRow(label='USBL', value='YES'))
        self.add_widget(InfoRow(label='IMU', value='YES'))
        self.add_widget(InfoRow(label='Pressure sensor', value='YES'))
        self.add_widget(InfoRow(label='Temp sensor', value='YES'))

        overview_title = SectionTitle(local_title='Connections')
        overview_title.height = 30

        self.add_widget(overview_title)
        self.add_widget(InfoRow(label='Fiber', value='YES'))
        self.add_widget(InfoRow(label='Serial', value='YES'))
        self.add_widget(InfoRow(label='3G', value='NO'))
        self.add_widget(InfoRow(label='WiFi', value='NO'))


class ConfigurationFrame(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(ConfigurationFrame, self).__init__(**kwargs)

        self.orientation = 'horizontal'

        sensors = SensorsFrame()

        splitter = Splitter(sizable_from='right')
        splitter.add_widget(sensors)

        self.add_widget(splitter)
