# -*- coding: utf-8 -*-

import numpy as np


def gennormalizedwavepackage(start=-50, end=50, resolution=1, mi=0, sig=1):
    resolution = int(resolution)
    res = []
    A = 1/np.sqrt(2 * pow(sig, 2) * np.pi)
    for x in range(start*resolution, end):
        res.append(A * np.exp(-pow(x/resolution - mi, 2) / (2 * pow(sig, 2))))
    return res


def gensinwave(start=-50, end=50, resolution=1, amplitude=1, freq=1, phase=0):
    resolution = int(resolution)
    res = []
    for i in range(start*resolution, end*resolution):
        x = float(i)/float(resolution)
        res.append(amplitude*np.sin(freq*x + phase))
    return res


def fourrierTransform(f):
    return np.fft.fft(f)
