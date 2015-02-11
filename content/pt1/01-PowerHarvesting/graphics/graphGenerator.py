import sys
import os
sys.path.append('/home/mark/Dropbox/University/PhD/Workbench/electrodeInterface/')
import lib.plot.formatter
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt


# zeta = -62.2e-3 # Volts
eta_water_rel = 80.1 # Farads per meter @ ~ 20degC
eta_absolute = 8.854187817e-12 # Farads per meter

eta = eta_water_rel * eta_absolute # Absolute permittiviy of water

mu = 1.002e-3 # Pascals second
cond = 0.017 # Siemens per meter
cond = 18.9e-3 # Siemens per meter
cond = 17.0e-3 #Siemens per meter
# print("zeta = %0.3f" % zeta)
print("eta_water_rel = %0.3f" % eta_water_rel)
print("eta_absolute = %0.3e" % eta_absolute)
print("mu = %0.3e" % mu)


path = './data'
# heights = [26, 52, 56, 71, 75, 106, 125, 161, 178, 245]
heights = []
data = {}
for filename in os.listdir(path):
    datum = {'pressure':[], 'voltage':[]}

    correction = 0
    #apply y-shift corrections
    if filename[:-10] == '245':
        correction = float(-0.0273512001237602)
    elif filename[:-10] == '178':
        correction = float(-0.0132851668915389)
    elif filename[:-10] == '161':
        correction = float(-0.0230450198187396)
    elif filename[:-10] == '125':
        correction = float(0.00540160076385972)
    elif filename[:-10] == '106':
        correction = float(0.0575546965675481)
    elif filename[:-10] == '75':
        correction = float(-0.0197771186509623)
    elif filename[:-10] == '71':
        correction = float(0.0444167406200488)
    elif filename[:-10] == '56':
        correction = float(0.405002719780868)
    elif filename[:-10] == '52':
        correction = float(0.0234330092033605)
    elif filename[:-10] == '26':
        correction = float(0.0380312475791444)
    # correction = 0
    with open(path + '/' + filename, 'r') as f:
        f.readline()
        for line in f.readlines():
            parts = line.split(',')
            pressure = 1.0 * (float(parts[0])*6.89475729)
            voltage = 1.0 * (float(parts[1])-correction)
            if pressure > 0:
                datum['pressure'].append(pressure)
                datum['voltage'].append(voltage)
        height = int(filename.split('um')[0])
        heights.append(height)
        data[height] = datum

heights.sort()
ys_comp = []
xs_comp = []
xs_pvh = []
ys_pvh = []
# heights.remove(56)

for height in heights:
    xs_pvh_run = []
    ys_pvh_run = []
    xs_comp_run = []
    ys_comp_run = []
    for press, voltage in zip(data[height]['pressure'],data[height]['voltage']):
        delta = height * 1e-6
        print("(%0.2e x %0.2e) / (%0.2e * %0.2e * %0.2e)" % (eta, press, mu, voltage, cond))
        y = (eta * (-1000 * press)) / (mu * voltage * cond)
        x = 1.0 / delta

        ys_pvh_run.append(voltage)
        xs_pvh_run.append(press)
        if press > 100:
            xs_comp_run.append(x)
            ys_comp_run.append(y)
        # print("%0.3e %0.3e %0.3e"% (delta, press, voltage))
    xs_pvh.append(xs_pvh_run)
    ys_pvh.append(ys_pvh_run)
    xs_comp.append(xs_comp_run)
    ys_comp.append(ys_comp_run)

markers = ['o', 'd', 'x', 'v']
colours = lib.plot.formatter.get_reds(len(heights))
print(colours)
lib.plot.formatter.format(style='Thesis')

# for index, (xs, ys) in enumerate(zip(xs_pvh, ys_pvh)):
#     print(index * 0.1)
#     plt.plot(xs, ys, label='\SI{' + str(heights[index]) + '}{\micro\meter}', color=str(index * 0.1), marker=markers[index%len(markers)], mec=str(index*0.1), markersize=4)
# plt.gca().set_xlabel("Pressure (kPa)")
# plt.gca().set_ylabel("Voltage (mV)")
# plt.gca().set_xlim(0,320)
# plt.gca().set_ylim(-0.1,0.9)
# plt.legend(frameon=False, loc=0, ncol=2)
# plt.savefig(filename='graph_streamingVoltageGradient_vs_height.pdf', format='pdf')

# plt.clf()
# lib.plot.formatter.plot_params['margin']['left'] = 0.12
# lib.plot.formatter.format(style='Thesis')

for index, (xs, ys) in enumerate(zip(xs_comp, ys_comp)):
    plt.scatter(xs, ys, label='\SI{' + str(heights[index]) + '}{\micro\meter}', color=str(index * 0.1), marker=markers[index%len(markers)])
plt.gca().set_xlabel("$1/\delta$ (\SI{}{\per\meter})")
plt.gca().set_ylabel("$\\normalfont{\\varepsilon_{r}\\varepsilon_{0}\\Delta P / \\mu V_{s}\\sigma}$ (\\SI{}{\\per\\volt})")
plt.gca().set_ylim(-100,0)
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '%1.0f' % (x)))
plt.legend(frameon=False, loc=0, ncol=2)
plt.savefig(filename='graph_streamingComparison_gu.pdf', format='pdf')
# print(data)
# sys.exit()

# data_height_um_slope_mvPsi = [
#     [0.245, 0.0031649193],
#     [0.178, 0.0032297521],
#     [0.161, 0.0045257505],
#     [0.125, 0.0046819299],
#     [0.106, 0.0071909101],
#     [0.075, 0.0064584454],
#     [0.071, 0.0077858818],
#     [0.056, 0.0069451427],
#     [0.052, 0.0079515149],
#     [0.026, 0.0041040953],
# ]

# data_height_um_slope_V_per_kPa = []
# for row in data_height_um_slope_mvPsi:
#     data_height_um_slope_V_per_kPa.append([row[0], (row[1]/6.89475729)/1000.0])

# for row in data_height_um_slope_V_per_kPa:
#     print("%0.3f %0.3f" % (row[0], row[1]))



# ys = []
# xs = []
# for row in data_height_um_slope_V_per_kPa:
#     slope = row[1]
#     height = row[0] / 1000.0
#     x = 1.0/height
#     if x < 25000:
#         y = eta_absolute * eta_water_rel * (-1.0/slope) * (1.0/mu) * (1.0/cond)
#         print("%0.3e x 1")
#         ys.append(y)

#         xs.append(x)

# # lib.plot.formatter.format(style='Thesis')
# plt.scatter(xs,ys)
# plt.gca().set_xlabel("$1/\delta$ (1/m)")
# # plt.gca().set_ylim(-1e-7,0)
# plt.show()