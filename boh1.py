from kivy.app import App

from kivy.uix.tabbedpanel import TabbedPanel


class Test(TabbedPanel):
    pass


class MyApp(App):

    def __init__(self):
        super(MyApp, self).__init__()
        self.base_view = Test()

    def build(self):
        return self.base_view


if __name__ == '__main__':
    from kivy.core.window import Window

    Window.size = (1280, 800)
    MyApp().run()