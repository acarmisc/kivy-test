from os.path import expanduser, sep, dirname

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooser, FileChooserListLayout, platform, FileChooserIconView
from kivy.uix.splitter import Splitter
from kivy.uix.videoplayer import VideoPlayer


class BrowserFrame(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(BrowserFrame, self).__init__(**kwargs)

        self.orientation = 'vertical'

        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileChooserIconView(select_string='Select',
                                      favorites=[(user_path, 'Documents')])

        browser.path = './'
        browser.bind(
            on_success=self._fbrowser_success,
            on_canceled=self._fbrowser_canceled)

        self.add_widget(browser)

    def _fbrowser_canceled(self, instance):
        print 'cancelled, Close self.'

    def _fbrowser_success(self, instance):
        print instance.selection


class VideoFrame(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(VideoFrame, self).__init__(**kwargs)

        self.orientation = 'horizontal'

        sensors = BrowserFrame()

        splitter = Splitter(sizable_from='right')
        splitter.add_widget(sensors)
        self.add_widget(splitter)

        player = VideoPlayer(source='./GoPro/test.mp4', state='play',
                             options={'allow_stretch': True})

        self.add_widget(player)