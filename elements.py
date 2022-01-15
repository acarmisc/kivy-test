import time

from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput

from config import ColorScheme
from data import data


class HexColor(Color):

    def __init__(self, code, a=1):
        super(Color, self).__init__()
        code = code.lstrip('#')

        r, g, b = tuple(int(code[i:i + 2], 16) for i in (0, 2, 4))

        Color(r / 255.0, g / 255.0, b / 255.0, a)
        self.channels = [r, g, b, a]


class FileFinder(GridLayout):

    def __init__(self, **kwargs):
        super(FileFinder, self).__init__(**kwargs)

        self.cols = 3
        self.add_widget(Label(text=kwargs['label']))
        self.add_widget(TextInput(text='.', multiline=False))
        self.add_widget(Button(text='..'))


class WelcomeLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        self.orientation = 'vertical'

        super(WelcomeLayout, self).__init__(**kwargs)

        self.color = HexColor(ColorScheme.MAIN_TEXT_COLOR).channels

        title = AppTitle()
        subtitle = Label(text='Select data folder to create a mission DB', font_size='30sp', halign='right')
        subtitle.size_hint_y = 0.5

        self.add_widget(title)
        self.add_widget(subtitle)
        self.add_widget(ProgressBar(max=1000))
        raw_data = FileFinder(label='Raw data location: ')
        raw_data.size_hint_y = 0.2
        raw_data.padding = 5
        self.add_widget(raw_data)

        to_data = FileFinder(label='Save db to: ')
        to_data.size_hint_y = 0.2
        to_data.padding = 5
        self.add_widget(to_data)

        btn_next = Button(text='Next')
        btn_next.size_hint_y = 0.2

        self.add_widget(btn_next)

        pb = ProgressBar(max=1000)
        self.add_widget(pb)

        pb.value = 750


class LabelRow(GridLayout):
    def __init__(self, *args, **kwargs):
        background_color = kwargs.pop('background_color', '#476685')
        background_alpha = kwargs.pop('background_alpha', 1)
        self.size_hint_y = 0.3

        super(LabelRow, self).__init__(*args, **kwargs)

        with self.canvas.before:
            HexColor(background_color, background_alpha)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class BadgeLabel(Label):

    def __init__(self, *args, **kwargs):
        background_color = kwargs.pop('background_color', ColorScheme.BACKGROUND_COLOR)
        background_alpha = kwargs.pop('background_alpha', 1)
        self.size_hint_y = 0.3
        super(BadgeLabel, self).__init__(*args, **kwargs)

        with self.canvas.before:
            HexColor(background_color, background_alpha)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update(self, msg, color, timeout=3):
        self.text = msg
        with self.canvas.before:
            HexColor(color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            Clock.schedule_once(self._reset_label, timeout)


def _reset_label(self, _):
    self.text = 'Waiting for badge'
    self.color = HexColor(ColorScheme.FONT_COLOR).channels

    with self.canvas.before:
        HexColor(ColorScheme.BACKGROUND_COLOR)
        self.rect = Rectangle(size=self.size, pos=self.pos)


class TimelineSlider(GridLayout):

    def __init__(self, *args, **kwargs):
        from kivy.uix.slider import Slider
        super(TimelineSlider, self).__init__(**kwargs)

        self.cols = 2

        s = Slider(min=-100, max=100, value=25)
        lbl = Label(text='Mission review')

        lbl = Label(text='Mission review')

        self.add_widget(s)
        self.add_widget(lbl)


class CoordinatesView(GridLayout):

    def __init__(self, *args, **kwargs):
        super(CoordinatesView, self).__init__(*args, **kwargs)

        self.cols = 1

        self.bind(minimum_height=self.setter('height'))

        for i in data:
            btn = Label(text=str((i[0], i[1])), size_hint_y=None, height=40)
            self.add_widget(btn)


class StatusBar(LabelRow):

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)

        self.cols = 3

        db_path = Label(text='/Users/andrea/Documents/S3M/002', font_size='15dp')

        db_size = Label(text='4.3 GB', font_size='15dp')

        duration = Label(text='0 hrs 34 mins', font_size='15dp')

        self.add_widget(db_path)
        self.add_widget(db_size)
        self.add_widget(duration)


class AppTitle(LabelRow):

    def __init__(self, **kwargs):
        super(AppTitle, self).__init__(**kwargs)

        self.cols = 1

        text = Label(text='S3MAG Mission Review', font_size='50dp', )

        text.halign = 'left'
        self.add_widget(text)


class SectionSubTitle(LabelRow):

    def __init__(self, **kwargs):
        super(SectionSubTitle, self).__init__(**kwargs)

        background_color = ColorScheme.BACKGROUND_COLOR_SUB
        with self.canvas.before:
            HexColor(background_color, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.cols = 1

        text = Label(text=kwargs['local_title'], font_size='18dp', )

        text.halign = 'left'
        self.add_widget(text)


class SectionTitle(LabelRow):

    def __init__(self, **kwargs):
        super(SectionTitle, self).__init__(**kwargs)

        self.cols = 1

        text = Label(text=kwargs['local_title'], font_size='25sp', )

        text.halign = 'left'
        self.add_widget(text)


class InfoRow(GridLayout):

    def __init__(self, *args, **kwargs):
        super(InfoRow, self).__init__(*args, **kwargs)

        background_color = kwargs.pop('background_color', ColorScheme.BACKGROUND_COLOR_ALT)
        background_alpha = kwargs.pop('background_alpha', 1)
        self.size_hint_y = 0.3
        self.cols = 2

        with self.canvas.before:
            HexColor(background_color, background_alpha)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        label = Label(text=kwargs['label'])

        label.color = HexColor(ColorScheme.FONT_COLOR).channels
        label.size_hint_x = 0.2
        label.text_size = (80, None)
        label.halign = 'left'

        value = Label(text=kwargs['value'])
        value.text_size = (80, None)
        value.color = HexColor(ColorScheme.VALUE_COLOR).channels

        self.add_widget(label)
        self.add_widget(value)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class TableHeader(Label):

    def __init__(self, *args, **kwargs):
        super(TableHeader, self).__init__(**kwargs)

        self.font_size = '11dp'
        self.padding = (1, 1)

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            HexColor(ColorScheme.VALUE_COLOR, 1)
            Rectangle(pos=self.pos, size=self.size)


class TableValue(Label):

    def __init__(self, *args, **kwargs):
        super(TableValue, self).__init__(**kwargs)

        self.font_size = '9dp'

        self.size_hint_y = 0.5
        self.padding = (1, 1)

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            HexColor(ColorScheme.BACKGROUND_COLOR, 1)
            Rectangle(pos=self.pos, size=self.size)


class DataTable(GridLayout):

    def __init__(self, **kwargs):
        super(DataTable, self).__init__(**kwargs)

        self.cols = 1
        self.spacing = 1

        data = kwargs.get('data')

        col_names = list(data.columns.values)

        table = GridLayout(cols=len(col_names))
        for n in col_names:
            table.add_widget(TableHeader(text=n))

        for index, row in data.iterrows():
            for n in col_names:
                table.add_widget(TableValue(text=str(row[n])))

        self.add_widget(table)


class EmptyFrame(GridLayout):

    def __init__(self, **kwargs):
        super(EmptyFrame, self).__init__(**kwargs)

        self.cols = 1

        self.add_widget(Label(text='Empty'))
        import random
