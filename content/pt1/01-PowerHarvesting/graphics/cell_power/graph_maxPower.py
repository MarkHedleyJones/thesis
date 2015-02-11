import os
import sys
import matplotlib.pyplot as plt

sys.path.append('/home/mark/Dropbox/University/PhD/Workbench/electrodeInterface/')
import lib.plot.formatter
lib.plot.formatter.plot_params['margin']['left'] = 0.09
lib.plot.formatter.plot_params['margin']['bottom'] = 0.15
lib.plot.formatter.plot_params['margin']['right'] = 0.02
lib.plot.formatter.plot_params['margin']['top'] = 0.03
lib.plot.formatter.plot_params['ratio'] /= 2.5
lib.plot.formatter.format(style='Thesis')

times = []
currents = []
pressures = []
voltages = []
powers = []
with open('streamingCells_1411696812_cell9_cold_currentSweep_maxPower.csv', 'r') as f:
    header = f.readline()
    line = f.readline()
    while line:
        time, current, voltage, pressure, power = map(float,line.split(','))
        line = f.readline()
        times.append(time)
        currents.append(-current)
        voltages.append(voltage)
        pressures.append(pressure)
        powers.append(-power)


currents = list(map(lambda x: x * 1e9, currents))

plt.subplot(3,1,1)
plt.gca().set_ylabel('Applied pressure (\\SI{}{\\kilo\\pascal})')
plt.gca().set_ylim(0,300)
plt.plot(currents, pressures, label="Pressure", color='black')
plt.grid()
for loc, spine in list(plt.gca().spines.items()):        # For python 3
    if loc in ['right', 'top']:
        spine.set_color('none')  # don't draw spine

plt.subplot(3,1,2)
plt.gca().set_ylabel('Streaming voltage (\\SI{}{\\milli\\volt})')
plt.gca().set_ylim(0,500)
plt.plot(currents, list(map(lambda x: x * 1000.0, voltages)), label="Voltage", color='black')
for loc, spine in list(plt.gca().spines.items()):        # For python 3
    if loc in ['right', 'top']:
        spine.set_color('none')  # don't draw spine
plt.grid()

plt.subplot(3,1,3)
plt.plot(currents, list(map(lambda x: x * 1.0e9, powers)), label="Power", color='black')
plt.gca().set_ylim(0,2)
plt.gca().set_ylabel('Output power (\\SI{}{\\nano\\watt})')
plt.gca().set_xlabel('Drawn current (\\SI{}{\\nano\\ampere})')
for loc, spine in list(plt.gca().spines.items()):        # For python 3
    if loc in ['right', 'top']:
        spine.set_color('none')  # don't draw spine
plt.grid()


plt.tight_layout()


plt.savefig('../graph_streamingCell_outputPower_resistanceSweep.pdf', format='pdf')
