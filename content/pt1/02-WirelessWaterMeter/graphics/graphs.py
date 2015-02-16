#! /bin/python2
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import integrate
from matplotlib.ticker import FuncFormatter
import sys
import functools

plotting = True


sys.path.append('/home/mark/Dropbox/University/PhD/Workbench/electrodeInterface/')
import lib.plot.formatter


# def toilet_litre_per_second_at_second(x, start=3000, duration=80, rate=15, max_flow=0.1):
def toilet_litre_per_second_at_second(x, start=0, duration=80, rate=18, max_flow=0.1):
    end = start + duration
    if start < x < start + duration:
        val = max_flow-max_flow*math.exp((x-end)/rate)
        if val < 0:
            val = 0
    else:
        val = 0
    return val


# def shower_litre_per_second_at_second(x, start=900, duration=396.0, flow=0.125):
def shower_litre_per_second_at_second(x, start=0, duration=396.0, flow=0.125):
    if start < x < (start + duration):
        val = flow
    else:
        val = 0
    return val

# def washing_litre_per_second_at_second(x, start=100, flow=0.122):
def washing_litre_per_second_at_second(x, start=0, flow=0.122):
    fill_time_min = 18.0
    cycle1_start = start
    cycle1_end = cycle1_start + fill_time_min*60.0
    cycle2_start = cycle1_end + 20*60.0
    cycle2_end = cycle2_start + fill_time_min*60.0

    if cycle1_start < x < cycle1_end:
        val = flow
    elif cycle2_start < x < cycle2_end:
        val = flow
    else:
        val = 0

    return val


## Calculate the amount of energy in each event


# def pressure_loss_MPa(flow_m3_hour):
#     if flow_m3_hour == 0:
#         return 0
#     flow_litre_per_hour = flow_m3_hour * 1000.0
#     # Trend line obtained from fitting a 2-degree polynomial equation to
#     # points read of the pressure loss graphic.
#     # Flow is given in m^3/h and pressure is in MPa
#     result = 0.00316*math.pow(flow_m3_hour,2) + 0.00331*flow_m3_hour + 0.00235

#     # result = math.exp(3.725 * math.log(flow_litre_per_hour) - 9.5) / 1000.0
#     return result

def litres_as_cubic_meters(litre):
    return litre * 0.001

def cubic_meters_as_litres(cubic_meter):
    return cubic_meter * 1000.0

def megas_as_kilos(mega):
    return mega * 1000.0

def kilos_as_units(kilo):
    return kilo * 1000.0

def megas_as_units(mega):
    return kilos_as_units(megas_as_kilos(mega))

def units_as_kilos(unit):
    return unit / 1000.0

def kilos_as_megas(kilo):
    return kilo / 1000.0

def units_as_megas(unit):
    return units_as_kilos(kilos_as_megas(unit))

def hours_as_minutes(hour):
    return hour * 60.0

def minutes_as_seconds(minute):
    return minute * 60.0

def hours_as_seconds(hour):
    return minutes_as_seconds(hours_as_minutes(hour))

def seconds_as_minutes(second):
    return second / 60.0

def minutes_as_hours(minute):
    return minute / 60.0

def seconds_as_hours(second):
    return minutes_as_hours(seconds_as_minutes(second))

def litre_per_hour_to_kilopascal(litre_per_hour):
    if litre_per_hour == 0:
        return 0
    return math.exp(3.725 * math.log(litre_per_hour,10) - 9.5)

def flow_pressure_to_power(cubic_meter_per_second, pascal):
    return cubic_meter_per_second * pascal


def pressure_loss_MPa(flow_m3_hour):
    if flow_m3_hour == 0:
        return 0
    flow_litre_per_hour = flow_m3_hour * 1000.0
    # Trend line obtained from fitting a 2-degree polynomial equation to
    # points read of the pressure loss graphic.
    # Flow is given in m^3/h and pressure is in MPa
    result = 0.00316*math.pow(flow_m3_hour,2) + 0.00331*flow_m3_hour + 0.00235

    # result = math.exp(3.725 * math.log(flow_litre_per_hour) - 9.5) / 1000.0
    return result


class Appliance:

    function_litre_per_second_at_second = None

    def __init__(self, function):
        self.function_litre_per_second_at_second = function

    def litre_per_second_at_second(self, second):
        return self.function_litre_per_second_at_second(second)

    def litre_per_minute_at_second(self, second):
        return self.litre_per_second_at_second(second) * 60.0

    def pascal_at_second(self, second):
        lpm = self.litre_per_minute_at_second(second)
        lph = lpm * 60.0 # 60 minutes in an hour
        kpa = litre_per_hour_to_kilopascal(lph)
        pa = kpa * 1000.0 # 1000 pascals in a kilopascal
        return pa

    def cubic_meter_per_second_at_second(self, second):
        lps = self.litre_per_second_at_second(second)
        cmps = lps / 1000.0 # 1000 litres in a cubic meter
        return cmps

    def watt_at_second(self, second):
        pa = self.pascal_at_second(second)
        cmps = self.cubic_meter_per_second_at_second(second)
        watts = flow_pressure_to_power(cmps, pa)
        return watts


profile_appliances = {
    'shower': Appliance(functools.partial(shower_litre_per_second_at_second, start=60*23)),
    'toilet': Appliance(functools.partial(toilet_litre_per_second_at_second, start=60*35)),
    'washing': Appliance(functools.partial(washing_litre_per_second_at_second, start=60 * 2))
}

appliances = {
    'shower': Appliance(shower_litre_per_second_at_second),
    'toilet': Appliance(toilet_litre_per_second_at_second),
    'washing': Appliance(washing_litre_per_second_at_second)
}

# if plotting:

#     lib.plot.formatter.plot_params['margin']['left'] = 0.10
#     lib.plot.formatter.plot_params['margin']['bottom'] = 0.135
#     lib.plot.formatter.plot_params['margin']['right'] = 0.02
#     lib.plot.formatter.plot_params['margin']['top'] = 0.03
#     lib.plot.formatter.format(style='Thesis')
#     ax = plt.gca()
#     ax.set_xlabel('Time (\\SI{}{\\minute})')
#     ax.set_ylabel('Flow (\\SI{}{\\litre\\per\\min})')
#     ax.set_ylim(0,8.5)

#     xs = list(range(60 * 60))

#     plt.plot(xs, list(map(profile_appliances['washing'].litre_per_minute_at_second, xs)), label='Washing machine', linestyle='-', color='0')
#     plt.plot(xs, list(map(profile_appliances['shower'].litre_per_minute_at_second, xs)), label='Shower', linestyle='--', color='0.66')
#     plt.plot(xs, list(map(profile_appliances['toilet'].litre_per_minute_at_second, xs)), label='Toilet', linestyle=':', color='0.33')
#     plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, pos: '%1.0f' % (x / 60.0)))
#     plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '%1.1f' % (x)))
#     plt.gca().set_xticks(list(map(lambda x: x * 600.0, range(0, 7))))
#     plt.legend(frameon=False, ncol=3)
#     plt.savefig('graph_profile.pdf', format='pdf')


# if plotting:
#     plt.clf()
#     lib.plot.formatter.plot_params['margin']['left'] = 0.10
#     lib.plot.formatter.plot_params['margin']['bottom'] = 0.135
#     lib.plot.formatter.plot_params['margin']['right'] = 0.02
#     lib.plot.formatter.plot_params['margin']['top'] = 0.04
#     lib.plot.formatter.format(style='Thesis')
#     ax = plt.gca()
#     ax.set_xlabel('Time (\\SI{}{\\minute})')
#     ax.set_ylabel('Power (\\SI{}{\\milli\\watt})')
#     plt.gca().set_ylim(0,0.210)

#     xs = list(range(60 * 60))

#     plt.plot(xs, list(map(profile_appliances['washing'].watt_at_second, xs)), label='Washing', linestyle='-', color='0')
#     plt.plot(xs, list(map(profile_appliances['shower'].watt_at_second, xs)), label='Shower', linestyle='--', color='0.66')
#     plt.plot(xs, list(map(profile_appliances['toilet'].watt_at_second, xs)), label='Toilet', linestyle=':', color='0.33')
#     plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, pos: '%1.0f' % (x / 60.0)))
#     plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '%1.0f' % (x * 1000)))
#     plt.gca().set_xticks(list(map(lambda x: x * 600.0, range(0, 7))))
#     plt.legend(frameon=False, ncol=3)
#     plt.savefig('graph_harvest.pdf', format='pdf')


print('washing machine volume = %0.2f l' % integrate.quad(appliances['washing'].litre_per_second_at_second, 0, 1000)[0])
print('shower volume = %0.2f l' % integrate.quad(appliances['shower'].litre_per_second_at_second, 0, 1000)[0])
print('toilet volume = %0.2f l' % integrate.quad(appliances['toilet'].litre_per_second_at_second, 0, 1000)[0])

print('washing machine energy = %0.2f l' % integrate.quad(appliances['washing'].watt_at_second, 0, 1000)[0])
print('shower energy = %0.2f l' % integrate.quad(appliances['shower'].watt_at_second, 0, 1000)[0])
print('toilet energy = %0.2f l' % integrate.quad(appliances['toilet'].watt_at_second, 0, 1000)[0])


if plotting:
    plt.clf()
    lib.plot.formatter.plot_params['margin']['left'] = 0.10
    lib.plot.formatter.plot_params['margin']['bottom'] = 0.15
    lib.plot.formatter.format(style='Thesis')

    xs = list(range(0,20))
    ys = list(map(litre_per_hour_to_kilopascal, map(lambda x: x * 60,xs)))
    # plt.gca().set_xlabel('Flow (\\SI{}{\\cubic\\meter\\per\\hour})')
    plt.gca().set_xlabel('Flow through meter (\\SI{}{\\litre\\per\\minute})')
    plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, pos: '%1.f' % (x)))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '%1.1f' % (x)))
    # plt.gca().set_xlim(0.0, 10.0 / 16.66)
    # plt.gca().set_ylim(0.0, 20.0 / 1000.0)
    plt.gca().set_ylabel('Pressure drop (\\SI{}{\\kilo\\pascal})')
    plt.grid()
    plt.plot(xs,ys, color='black')
    # plt.tight_layout()
    plt.savefig('graph_pressureLoss.pdf', format='pdf')

# # sys.exit()
# # Pressure vs slope
# # 1 PSI = 6 894.75729 Pa

# height_slope = [
#     (0.245, 0.0031649193),
#     (0.178, 0.0032297521),
#     (0.161, 0.0045257505),
#     (0.125, 0.0046819299),
#     (0.106, 0.0071909101),
#     (0.075, 0.0064584454),
#     (0.071, 0.0077858818),
#     (0.056, 0.0069451427),
#     (0.052, 0.0079515149),
#     (0.026, 0.0041040953)
# ]

# height = list(map(lambda x: x[0] * 1000, height_slope))
# slope = list(map(lambda x: (x[1] * 1000000) / 6894.75729, height_slope))

# # print("Slope of " +str(height[-2]) + " is " + str(slope[-2]))
# slope_52 = slope[-2]

# if plotting:
#     plt.clf()
#     lib.plot.formatter.plot_params['margin']['left'] = 0.1
#     lib.plot.formatter.plot_params['margin']['bottom'] = 0.15
#     lib.plot.formatter.plot_params['margin']['right'] = 0.026
#     lib.plot.formatter.plot_params['margin']['top'] = 0.03
#     lib.plot.formatter.format(style='Thesis')
#     plt.gca().set_xlabel('Channel height ($\mu$m)')
#     plt.gca().set_ylabel('Voltage-pressure gradient ($\mu$V/Pa)')
#     plt.scatter(height,slope, marker='o', facecolor='blue', edgecolor='blue', s=8)
#     plt.gca().set_xlim(0,250)
#     plt.gca().set_ylim(0,1.201)
#     plt.grid()
#     plt.savefig('graph_cellEfficiency.pdf', format='pdf')

# pressure_voltage = [
#     (5.0111, 0.0627),
#     (6.0244, 0.0708),
#     (7.0013, 0.0779),
#     (8.0006, 0.0858),
#     (8.9845, 0.0944),
#     (9.9992, 0.1025),
#     (11.025, 0.1111),
#     (12.048, 0.1202),
#     (13.057, 0.1291),
#     (14.037, 0.1367),
#     (14.978, 0.144),
#     (16.002, 0.1523),
#     (16.966, 0.1589),
#     (18.02,  0.1674),
#     (18.989, 0.1744),
#     (20.031, 0.1834),
#     (20.937, 0.1907),
#     (21.914, 0.1981),
#     (22.962, 0.2038),
#     (24.103, 0.2135),
#     (25.024, 0.2223),
#     (26.008, 0.2294),
#     (27.061, 0.2386),
#     (27.806, 0.2404),
#     (28.996, 0.253),
#     (29.869, 0.2609),
#     (30.776, 0.2686),
#     (31.756, 0.2764),
#     (32.791, 0.2852),
#     (33.945, 0.2943),
#     (35.193, 0.3045),
#     (35.887, 0.31),
#     (36.621, 0.3122),
#     (38.362, 0.3293)
# ]

# # Naughty correction pulls the y-intercept down to 0V at 0 Pa.
# # Yes, it is bad to do this but hey, this is the least of this paper's problems.
# naughty_correction = 0.0234330092033605

# voltage = list(map(lambda x: (x[1] - naughty_correction) * 1000.0, pressure_voltage))
# pressure = list(map(lambda x: (x[0] * 6894.75729)/1000.0, pressure_voltage))


# if plotting:
#     for volt, press in zip(voltage, pressure):
#         # slope_52 is in uV per Pa
#         # press is in kPa
#         applied_pressure = press * 1000
#         voltage_prediction_uV = applied_pressure * slope_52
#         voltage_prediction = voltage_prediction_uV / 1.0e6
#         voltage_actual = volt/1.0e3
#         diff = voltage_actual - voltage_prediction
#         print("At {2:.3f} Pa the channel should develop {0:.3f}V but actually develops {1:.3f}V ({3:.3f} difference)".format(voltage_prediction, voltage_actual, press, diff))

#     plt.clf()
#     lib.plot.formatter.plot_params['margin']['left'] = 0.11
#     lib.plot.formatter.plot_params['margin']['bottom'] = 0.15
#     lib.plot.formatter.plot_params['margin']['right'] = 0.026
#     lib.plot.formatter.plot_params['margin']['top'] = 0.03
#     lib.plot.formatter.format(style='Thesis')
#     plt.gca().set_xlabel('Pressure (kPa)')
#     plt.gca().set_ylabel('Streaming potential (mV)')
#     plt.grid()
#     plt.plot(pressure, voltage, marker='.', markersize=5)
#     # plt.gca().set_xlim(0,250)
#     plt.savefig('graph_voltagePressure.pdf', format='pdf')




# internal_resistance_ohm = 30.0e9
# # P=V*I
# voltage = list(map(lambda x: x / 1000.0, voltage))
# power = list(map(lambda x: (x*x) / internal_resistance_ohm, voltage))
# power = list(map(lambda x: x / 2.0, power))
# power = list(map(lambda x: x * 1e12, power))


# if plotting:
#     plt.clf()
#     lib.plot.formatter.plot_params['margin']['left'] = 0.11
#     lib.plot.formatter.plot_params['margin']['bottom'] = 0.15
#     lib.plot.formatter.plot_params['margin']['right'] = 0.026
#     lib.plot.formatter.plot_params['margin']['top'] = 0.06
#     lib.plot.formatter.format(style='Thesis')
#     plt.gca().set_xlabel('Pressure (\\SI{}{\\kilo\\pascal})')
#     plt.gca().set_ylabel('Output power (pW)')
#     plt.grid()
#     plt.scatter(pressure, power, color="black", edgecolor=None, s=5)
#     plt.gca().set_ylim(0,2)
#     plt.savefig('graph_powerPressure.pdf', format='pdf')

