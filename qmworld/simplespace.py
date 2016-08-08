import core, plot, numpy as np


class SimpleSpace:
    h = 1
    h_cort = h / (2 * np.pi)

    #espaço que depende apenas de x, não conta o tempo y(x) V(x)

    def __init__(self):
        self.x = []
        self.y = []
        self.V = []
        self.setx()
        self.wave()
        print self.x, self.y

    def shrodinger(self):
        return self.h_cort


    def setx(self, numelementos=100, inicio=0, resolucao=0.1):
        self.x = np.array(range(inicio, (numelementos - inicio))) * resolucao
        return self.x

    def wave(self,amp=1, freq=2, phase=0):
        Y = []
        for i in self.x:
            self.y.append(amp*np.cos(freq*i + phase))
        return self.y

    def addsteppotential(self):

    def show(self):
        plot.simplePlot(self)
