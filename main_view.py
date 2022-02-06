from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from elements import TimelineSlider, CoordinatesView, AppTitle
from graphs import GraphExample
from map_frame import MapFrame
from overview import OverviewFrame


class MainView(GridLayout):

    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(**kwargs)

        self.cols = 2

        m = MapFrame()
        self.add_widget(m)

        overview = OverviewFrame()
        self.add_widget(overview)

        #timeline = TimelineSlider()
        #self.add_widget(timeline)

        c = CoordinatesView(spacing=10, size_hint_y=None)
        coordinates = ScrollView(size_hint=(1, None), size=(Window.width, 100))
        coordinates.add_widget(c)
        self.add_widget(coordinates)

        #graph = GraphExample()
        #self.add_widget(graph)
