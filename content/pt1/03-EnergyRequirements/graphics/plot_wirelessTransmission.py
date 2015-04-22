import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import integrate
import sys
import os
import csv

sys.path.append('/home/mark/Dropbox/University/PhD/Workbench/electrodeInterface/')
import lib.plot.formatter

lib.plot.formatter.plot_params['margin']['left'] = 0.11
lib.plot.formatter.plot_params['margin']['bottom'] = 0.15
lib.plot.formatter.plot_params['margin']['right'] = 0.026
lib.plot.formatter.plot_params['margin']['top'] = 0.06
lib.plot.formatter.format(style='Thesis')

xs = []
ys = []
start = False
record = False
count = 0
with open('XBEE_Transmit_Power_10R2.csv') as csvfile:
    filereader = csv.reader(csvfile)
    for row in filereader:
        count += 1
        record = True
        if start and record:
            try:
                if count % 100 == 0:
                    print(row)
                    time = float(row[0])
                    power = float(row[2]) / 10.2 * float(row[1])
                    curr = float(row[4])
                    xs.append(time)
                    ys.append(power)
            except ValueError:
                pass
        else:
            if start is False:
                print(row)
                start = True

total = integrate.simps(ys,xs)
print("Total energy spent = {:}".format(total))

xs = list(map(lambda x: (x + 0.05)*1000, xs))
ys = list(map(lambda x: x * 1000, ys))
plt.gca().set_xlim(0,700)
plt.gca().set_ylim(0,50)
plt.gca().set_xlabel('Time (milliseconds)')
plt.gca().set_ylabel('Power (mW)')
plt.grid()
plt.plot(xs, ys, color='black', label="XBee Transmit ({:0.4f} Joule total)".format(total))
plt.legend(loc=0, frameon=False)
plt.savefig('Graph_XbeePower.pdf', format='pdf')

plt.clf()

### RFM ########################################################################

lib.plot.formatter.plot_params['margin']['left'] = 0.11
lib.plot.formatter.plot_params['margin']['bottom'] = 0.15
lib.plot.formatter.plot_params['margin']['right'] = 0.026
lib.plot.formatter.plot_params['margin']['top'] = 0.06
lib.plot.formatter.format(style='Thesis')

xs = []
ys = []
start = False
record = False
count = 0
with open('RFM_Transmit_Power_10R2.csv') as csvfile:
    filereader = csv.reader(csvfile)
    for row in filereader:
        count += 1
        record = True
        if start and record:
            try:
                if len(row) == 3:
                    if count % 100 == 0:
                        print(row)
                        time = float(row[0])
                        power = float(row[2]) / 10.2 * float(row[1])
                        # curr = float(row[4])
                        xs.append(time)
                        ys.append(power)
            except ValueError:
                pass
        else:
            if start is False:
                print('a')
                print(row)
                start = True

total = integrate.simps(ys,xs)
print("Total energy spent = {:}".format(total))

xs = list(map(lambda x: (x + 0.05)*1000, xs))
ys = list(map(lambda x: x * 1000, ys))

plt.gca().set_xlabel('Time (milliseconds)')
plt.gca().set_ylabel('Power (mW)')
plt.grid()
plt.gca().set_ylim(0,50)
plt.gca().set_xlim(0,700)
plt.plot(xs, ys, color='black', label="RFM Transmit ({:0.5f} Joule total)".format(total))
plt.legend(loc=0, frameon=False)
plt.savefig('Graph_RFMPower.pdf', format='pdf')

plt.clf()