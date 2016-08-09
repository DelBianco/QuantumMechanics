import core, plot, numpy as np


class SimpleSpace:
    h = 1
    h_cort = h / (2 * np.pi)

    def __init__(self):

        self.y = []
        self.V = []
        self.psy = []
        self.phi = []
        self.dt = 0.01
        self.dx = 0.01
        self.x = range(0, 1/self.dx, self.dx)
        self.gennormalizedwavepackage()

    def shrodinger(self):
        # TODO criar equacao de Schrodinger aqui para resolver
        # TODO verificar se a numpy possui as constantes, e verificar como ela trabalha com funcoes complexas

        # i hcort dParc_t psy(X,t) = - hcort^2 / 2m * Del^2 psy(X,t) + V(X,t)psy(X,t)

        return self.h_cort

    # deriva psy em relacao ao tempo
    def del_t_psy(self):
        dpsy = 0
        if len(self.psy) > 0:
            dpsy = []
            for t in range(len(self.psy)):
                dpsy.append((self.psy[t+1] - self.psy[t]) / self.dt)
        return dpsy

    def gennormalizedwavepackage(self, mi=1, sig=1):
        resolution = self.dx
        numpontos = int(1/self.dx)
        res = []
        A = 1 / np.sqrt(2 * pow(sig, 2) * np.pi)
        for x in range(numpontos):
            res.append(A * np.exp(-pow(x * resolution - float(mi), 2) / (2 * pow(sig, 2))))
        self.psy = res
        return res

    def wave(self, amp=1, freq=2, phase=0):
        Y = []
        for i in self.x:
            self.y.append(amp*np.cos(freq*i + phase))
        return self.y

    def show(self):
        plot.simplePlot(self)
