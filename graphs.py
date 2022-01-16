import random

from kivy.garden.pizza import Pizza
from kivy.garden.graph import MeshLinePlot, Graph, LinePlot
from kivy.uix.gridlayout import GridLayout
from numpy.ma import sin

from elements import InfoRow, SectionSubTitle


class GraphExample(GridLayout):

    def __init__(self, *args, **kwargs):
        super(GraphExample, self).__init__(*args, **kwargs)

        self.cols = 1

        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=10)
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        # values = ChData().data.ch1.tolist()
        # values = values[1:]
        # plot.points = [(100 , float(x)) for x in values]
        graph.add_plot(plot)

        self.add_widget(graph)


class MagnetometerGraph(GridLayout):

    def __init__(self, *args, **kwargs):
        super(MagnetometerGraph, self).__init__(*args, **kwargs)

        self.cols = 1

        data = kwargs.get('data')
        x_name = kwargs.get('x_name')
        y_names = kwargs.get('y_names')

        graph = Graph(xlabel=x_name, ylabel=str(y_names),
                      x_ticks_major=60, y_ticks_major=1000000,
                      y_grid_label=True, x_grid_label=True, padding=2,
                      x_grid=True, y_grid=True, xmin=-0, xmax=700, ymin=kwargs.get('ymin'),
                      ymax=kwargs.get('ymax'))

        graph.font_size = '10dp'

        for y_name in y_names:
            plot = LinePlot(color=[random.randint(50, 100) / 100.,
                                   random.randint(50, 100) / 100.,
                                   random.randint(50, 100) / 100.,
                                   random.randint(50, 100) / 100.], line_width=2)

            plot.points = []

            for index, row in data.iterrows():
                plot.points.append((float(row[x_name]), float(row[y_name])))

            #for i in range(0, 500):
            #    plot.points.append((i, random.randint(0, 2000000)))

            graph.add_plot(plot)

        self.add_widget(graph)


class MotorGraph(GridLayout):

    def __init__(self, *args, **kwargs):
        super(MotorGraph, self).__init__(*args, **kwargs)

        self.cols = 1

        data = kwargs.get('data')
        x_name = kwargs.get('x_name')
        y_names = kwargs.get('y_names')

        graph = Graph(xlabel=x_name, ylabel=str(y_names),
                      x_ticks_major=1, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=2,
                      x_grid=True, y_grid=True, xmin=-0, xmax=40, ymin=-1, ymax=120)

        graph.font_size = '10dp'

        for y_name in y_names:
            plot = LinePlot(color=[random.randint(50, 100) / 100.,
                                   random.randint(50, 100) / 100.,
                                   random.randint(50, 100) / 100.,
                                   random.randint(50, 100) / 100.], line_width=4)

            plot.points = []

        for index, row in data.iterrows():
            plot.points.append((float(row[x_name]), float(row[y_name])))

        #for i in range(0, random.randint(0, 40)):
        #    plot.points.append((i, float(random.randint(0,100))))

        graph.add_plot(plot)

        self.add_widget(graph)


class Modes(GridLayout):
    def __init__(self, *args, **kwargs):
        super(Modes, self).__init__(*args, **kwargs)

        self.cols = 2

        graph = GridLayout(cols=1)
        pie = Pizza(serie=[
            ["ROV", 75, 'f4aa42'],
            ["AUV", 25, '4262f4']],
            chart_size=128,
            legend_color='ffffcc',
            legend_value_rayon='50dp',
            legend_title_rayon='100dp',
            chart_border=1)

        graph.add_widget(pie)

        graph.padding = ['100dp', '40dp']

        values = GridLayout(cols=1)
        values.add_widget(SectionSubTitle(local_title='Values'))
        values.add_widget(InfoRow(label='AUV', value='25%'))
        values.add_widget(InfoRow(label='ROV', value='75%'))
        self.add_widget(values)
        self.add_widget(graph)
