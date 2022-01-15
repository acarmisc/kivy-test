from functools import partial

from kivy.core.window import Window
from kivy.garden.mapview.mapview.clustered_marker_layer import ClusteredMarkerLayer
from kivy.garden.mapview.mapview.view import MapView, MapMarker
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.splitter import Splitter

from data import data
from elements import CoordinatesView, SectionTitle, InfoRow


class MapFrame(GridLayout):

    def __init__(self, *args, **kwargs):
        super(MapFrame, self).__init__(**kwargs)

        self.cols = 1

        base_lon = 9.824520076125197
        base_lat = 44.05250694080099

        self.map = MapView(zoom=17, lon=base_lon, lat=base_lat)
        # self.map.size_hint_y = 50
        # self.map.size_hint_x = 0.30

        layer = ClusteredMarkerLayer()

        def on_press(*args, **kwargs):
            print(args)
            print(kwargs)
            print('ciao')

            for el in data:
                lon = el[0]
                lat = el[1]
                txt = 'bla'
                self.map.add_marker(MapMarker(lon=lon, lat=lat, source='marker.png', on_press=partial(on_press, txt)))

                # self.map.add_widget(layer)

        self.add_widget(self.map)


class MapExtendedFrame(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(MapExtendedFrame, self).__init__(**kwargs)

        self.orientation = 'horizontal'

        splitter = Splitter(sizable_from='right')
        base_lon = 9.824520076125197

        base_lat = 44.05250694080099

        self.map = MapView(zoom=8, lon=base_lon, lat=base_lat)

        def on_press(*args, **kwargs):
            # FIXME: set marker on blur
            print(args)

            item = args[1]
            item.source = 'assets/marker_focus.png'
            print(kwargs)
            print('ciao')

            for el in [(9.824520076125197, 44.05250694080099)]:
                lon = el[0]
                lat = el[1]
                txt = 'bla'
                self.map.add_marker(MapMarker(lon=lon, lat=lat, source='assets/marker1.png', on_press=partial(on_press,
                                                                                                              txt,
                                                                                                              self.map)))

        # self.map.add_widget(layer)

        splitter.add_widget(self.map)
        self.add_widget(splitter)

        point = PointDetails()
        self.add_widget(point)


class PointDetails(GridLayout):

    def __init__(self, **kwargs):
        super(PointDetails, self).__init__(**kwargs)

        self.cols = 1

        overview_title = SectionTitle(local_title='Single point details')
        overview_title.height = '30dp'
        self.add_widget(overview_title)

        self.add_widget(InfoRow(label='Coordinates', value='9.824520076,\n44.052506940'))

        self.add_widget(InfoRow(label='Time', value='09:04:12'))
        self.add_widget(InfoRow(label='Mode', value='AUV'))
        self.add_widget(InfoRow(label='Motor 1', value='0'))
        self.add_widget(InfoRow(label='Motor 2', value='0'))
        self.add_widget(InfoRow(label='Motor 3', value='0'))

        self.add_widget(InfoRow(label='Motor 4', value='0'))
        self.add_widget(InfoRow(label='Motor 5', value='0'))
        self.add_widget(InfoRow(label='Heading', value='0.000'))
        self.add_widget(InfoRow(label='Pitch', value='0.000'))
        self.add_widget(InfoRow(label='Roll', value='0.0000'))
        self.add_widget(InfoRow(label='Pression', value='0.000000 bar'))
        self.add_widget(InfoRow(label='Temperature', value='16.000000 C'))
        self.add_widget(InfoRow(label='Deep', value='-2'))
