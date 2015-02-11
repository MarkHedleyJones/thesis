import os
import sys
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
sys.path.append('/home/mark/Dropbox/University/PhD/Workbench/electrodeInterface/')
import lib.plot.formatter
lib.plot.formatter.plot_params['margin']['left'] = 0.09
lib.plot.formatter.plot_params['margin']['bottom'] = 0.15
lib.plot.formatter.plot_params['margin']['right'] = 0.02
lib.plot.formatter.plot_params['margin']['top'] = 0.03
lib.plot.formatter.plot_params['ratio'] /= 2.5


filenames = os.listdir('.')
filenames = list(filter(lambda x: x.find('_cold_'),filenames))
# print(filenames)
filenames = list(filter(lambda x: x[-4:] == '.csv', filenames))
filenames = list(filter(lambda x: x.find('ml_') != -1, filenames))
filenames.sort()

pp = PdfPages('all.pdf')

for filename in filenames:
    times = []
    currents = []
    pressures = []
    voltages = []
    powers = []
    with open(filename, 'r') as f:
        header = f.readline()
        line = f.readline()
        while line:
            time, current, voltage, pressure, power = list(map(float,line.split(',')))
            line = f.readline()
            times.append(time)
            if filename.find('currentSweep') != -1:
                current = current
                power = power
            currents.append(current)
            voltages.append(voltage)
            pressures.append(pressure)
            powers.append(power)

    times = [x - times[0] for x in times]

    plt.clf()
    lib.plot.formatter.format(style='Thesis')
    plt.subplot(4,1,3)

    plt.gca().set_ylabel('Current')
    plt.gca().set_ylim(0,1e-7)
    plt.plot(times, currents, label="Current")
    plt.gca().set_xlim(0,500)
    plt.grid()

    plt.subplot(4,1,2)
    plt.gca().set_ylabel('Voltage')
    plt.gca().set_ylim(0,0.5)
    plt.plot(times, voltages, label="Voltage")
    plt.gca().set_xlim(0,500)
    plt.grid()

    plt.subplot(4,1,1)

    title = ''
    parts = filename.split('_')
    for part in parts:
        if part.find('cell') != -1:
            title = part
    print(filename),
    print(title)
    plt.title(title)

    plt.gca().set_ylabel('Pressure')
    plt.gca().set_ylim(0,300)
    plt.plot(times, pressures, label="Pressure")
    plt.gca().set_xlim(0,500)
    plt.grid()

    plt.subplot(4,1,4)
    plt.plot(times, powers, label="Power")
    plt.gca().set_ylim(0,1e-8)
    plt.gca().set_ylabel('Power')
    plt.gca().set_xlim(0,500)
    plt.grid()


    plt.tight_layout()


    plt.savefig(pp, format='pdf')
pp.close()
