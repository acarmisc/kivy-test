# !/usr/bin/env python
from functools import partial
from random import random

from kivy.app import App
from kivy.core.window import Window
from kivy.garden.mapview.mapview.clustered_marker_layer import ClusteredMarkerLayer
from kivy.lang import Builder
from kivy.uix.actionbar import ActionBar
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.garden.mapview import MapView, MapMarker
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.video import Video
from kivy.factory import Factory as F

from data import data
from elements import TimelineSlider, CoordinatesView
from graphs import GraphExample
from logic import ChData
from map_frame import MapFrame


class BaseView(TabbedPanel):

    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)

        self.default_tab_text = 'Overview'

        main = MainView()
        self.default_tab_content = main

        th = TabbedPanelItem(text='Maps')
        th.add_widget(MapFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Mission log')
        th.add_widget(MapFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='?? Magnetic ??')
        th.add_widget(MapFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Idrophone ??? ')
        th.add_widget(MapFrame())
        self.add_widget(th)

        th = TabbedPanelItem(text='Video')
        th.add_widget(MapFrame())
        self.add_widget(th)


class MainView(GridLayout):

    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(**kwargs)

        self.cols = 1

        m = MapFrame()
        self.add_widget(m)

        timeline = TimelineSlider()
        self.add_widget(timeline)

        c = CoordinatesView(spacing=10, size_hint_y=None)
        coordinates = ScrollView(size_hint=(1, None), size=(Window.width, 100))
        coordinates.add_widget(c)
        self.add_widget(coordinates)

        graph = GraphExample()
        self.add_widget(graph)


class MyApp(App):

    def __init__(self):
        super(MyApp, self).__init__()

        self.base_view = BaseView()

    def build(self):
        return self.base_view


if __name__ == '__main__':
    from kivy.core.window import Window

    Window.size = (1280, 800)
    MyApp().run()
