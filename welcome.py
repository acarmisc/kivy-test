from kivy.app import App
from elements import WelcomeLayout


class MyApp(App):

    def build(self):
        return WelcomeLayout()


if __name__ == '__main__':
    MyApp().run()
