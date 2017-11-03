
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        #fig = Figure(figsize=(width, height), dpi=dpi)
        fig = plt.figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def plot(self, data):

        self.ax = self.figure.add_subplot(111)
        self.ax.clear()

        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")
        self.ax.set_xlim([0,24])
        self.ax.set_ylim([0,100])

        self.ax.plot(data, 'r-')
        self.ax.set_title('data')
        self.draw()


