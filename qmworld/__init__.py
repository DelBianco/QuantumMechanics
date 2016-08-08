import core
import plot

f = core.gennormalizedwavepackage()
f2 = core.gensinwave(0, 100, 10, 1, 10, 0)
print (f2)
# plot.simplePlot(f2)
plot.simplePlot(core.fourrierTransform(f2))
