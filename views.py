from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

from configuration import ConfigurationFrame
from elements import AppTitle, StatusBar, EmptyFrame
from magnetometer import MagnetometerFrame
from main_view import MainView
from map_frame import MapFrame, MapExtendedFrame
from mission import MissionLog
from motors import MotorsFrame
from raw_data import RawDataFrame
from video import VideoFrame


class BaseView(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)

        self.orientation = 'vertical'

        title = AppTitle()
        title.size_hint_y = 0.1

        status_bar = StatusBar()
        status_bar.size_hint_y = 0.05

        self.add_widget(title)
        self.add_widget(CoreView())
        self.add_widget(status_bar)


class CoreView(TabbedPanel):

    def __init__(self, *args, **kwargs):
        super(CoreView, self).__init__(*args, **kwargs)

        self.default_tab_text = 'Overview'

        main = MainView()
        self.default_tab_content = main

        th = TabbedPanelItem(text='Maps')
        th.add_widget(MapExtendedFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Mission log')
        th.add_widget(MissionLog())
        self.add_widget(th)

        th = TabbedPanelItem(text='Motors')
        th.add_widget(MotorsFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Magnetometer')
        th.add_widget(MagnetometerFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Hydrophone')
        th.add_widget(EmptyFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Video')
        th.add_widget(EmptyFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Configuration')
        th.add_widget(ConfigurationFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Raw data')
        th.add_widget(RawDataFrame())
        self.add_widget(th)


class MyApp(App):

    def __init__(self):
        super(MyApp, self).__init__()

        self.base_view = BaseView()

    def build(self):
        return self.base_view


if __name__ == '__main__':
    from kivy.core.window import Window

    #Window.size = (1280, 800)
    MyApp().run()