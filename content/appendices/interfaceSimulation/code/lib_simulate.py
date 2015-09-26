# Import required libraries
import numpy as np
import math
import mpmath
import subprocess
import threading
import os

# Optimised parameter repository
optimise = {}
optimise['cpe'] = {'slope':-0.79052566,
                   'mag':{'a':3284,
                          'b':-0.158}}
optimise['rs'] = {'a': 13.38,
                  'b':-0.8397}

command = None

def ladderResistorValues(conductivity):
    """
    Given a solution conductivity return suitable Rr Rv values
    (radial resistance (electrode) and vertical resistor commencing value,
    respecitvely)
    """
    Rr_b = 0.407  # Determined from optimisation
    Rv_b = 3.71  # Determined from optimisation
    Rr = Rr_b / conductivity
    Rv = Rv_b / conductivity
    return (Rr, Rv)


def rs(conc, a=None, b=None):
    """
    Given a concentration of PBS returns the value of Rs (The series resistance
    in the model)
    """
    if a is None:
        a = optimise['rs']['a']
    if b is None:
        b = optimise['rs']['b']
    return a * math.pow(conc, b)


def combine_subcircuitParallel(subCktA_name, subCktB_name, newName, rs=0.0):
    """
    Combines the provided two port subcircuits in parallel for easy
    use in a spice file.
    """
    out = ""
    out += "****************************************\n"
    out += "*   Combine " + subCktA_name + " and " + subCktB_name + " in\n"
    out += "*   parallel to provide " + newName + "\n"
    out += "****************************************\n"
    out += ".SUBCKT " + newName + " a b\n"
    out += "XC1 a mid " + subCktA_name + "\n"
    out += "XC2 a mid " + subCktB_name + "\n"
    out += "R1 mid b " + str(rs) + "\n"
    out += ".ENDS " + newName + "\n"
    return out


def generate_faradaicSubcircuit(conc,
                                params={},
                                i0=None,
                                n=None,
                                cm=None,
                                rm=None,
                                memristor=True):
    """
    Generates the ngspice compatible subcircuit named faradaic that simulates
    the faradic component in the interface. This includes the diode and
    memristor branches
    """

    # Load defaults
    i0 = 3.5e-7
    n = -0.025 * float(conc) + 0.164
    cm = 2.316e-04 + 1.224e-04 * math.exp(-conc / 6.832e-01)
    rm = 10000000.0

    if 'i0' in params:
        i0 = params['i0']
    if 'n' in params:
        n = params['n']
    if 'cm' in params:
        cm = params['cm']
    if 'rm' in params:
        rm = params['rm']

    if memristor:
        out = [".param i0=" + str(i0),
               ".param cm=" + str(cm),
               ".param rm=" + str(rm),
               ".param n=" + str(n),
               ".subckt faradaic n1 n2",
               "Bdm1 n1 n2 I=i0*exp(v(n1,n2)/n)",
               "Bdm2 n2 n1 I=i0*exp(v(n2,n1)/n)",
               "Bdm1cpy 0 mset I=i0*exp(v(n1,n2)/n)",
               "Bdm2cpy mset 0 I=i0*exp(v(n2,n1)/n)",
               "C_M mset 0 cm",
               "R_M mset 0 rm",
               ".ends"]
    else:
        out = [".param i0=" + str(i0),
               ".param cm=" + str(cm),
               ".param rm=" + str(rm),
               ".param n=" + str(n),
               ".subckt faradaic n1 n2",
               "Bdm1 n1 n2 I=i0*(1-v(mset))*exp(v(n1,n2)/n)",
               "Bdm2 n2 n1 I=i0*(1+v(mset))*exp(v(n2,n1)/n)",
               "Bdm1cpy 0 mset I=i0*(1-v(mset))*exp(v(n1,n2)/n)",
               "Bdm2cpy mset 0 I=i0*(1+v(mset))*exp(v(n2,n1)/n)",
               "C_M mset 0 cm",
               "R_M mset 0 rm",
               ".ends"]

    tmp = ""
    tmp += "****************************************\n"
    tmp += "*        Faradaic branch start         *\n"
    tmp += "****************************************\n"
    return (tmp + "\n".join(out) + "\n\n", 'faradaic')


def param_cpe_slope(conc):
    """
    Return the magnitude and slope of the CPE.
    """
    slope = optimise['cpe']['slope']
    mag = optimise['cpe']['mag']['a'] * math.pow(conc,
                                                 optimise['cpe']['mag']['b'])
    return (mag, slope)

def get_cpeParams(freq_min, freq_max, m, perDecade=3):
    """
    Calculates the parameters required to create a sufficiently accurate
    Constant Phase Element (CPE) from the given parameters.

    Returns (pts, k, y_theta) where:
        pts:     an array of frequencies at which to place RC elements
        k:       a parameter that controls multiplicity
        y_theta: another parameter, not sure of its exact definition
    """
    # Extend the range so no funny stuff happens at the endpoints
    freq_min /= 1000
    freq_max *= 1000

    # Calculate the number of elements to place in this range
    numPts = (math.log10(freq_max) - math.log10(freq_min)) * perDecade

    # Calculate the frequency scaling factor
    k_f = math.exp((math.log(freq_max) - math.log(freq_min)) / numPts)

    # Generate the x positions for cpe elements
    pts = []
    for i in range(int(numPts) + 1):
        pts.append(freq_min * math.pow(k_f, i))

    # Determine k - the multiplicity factor
    k = math.pow(k_f, 1 / m)

    # k gets used here to create the y_theta variables
    # which are passed to generate_fracpoleSubcircuit and used
    # to choose the value of capacitance in each RC branch.
    y_theta = ((math.pi / (m * math.log(k))) *
               mpmath.sec(0.5 * math.pi * (1 - (2 / m))))

    return (pts, y_theta)


def generate_fracpoleSubcircuit(conc, fmin, fmax, m=1.34):
    """
    Generates the ngspice compatible subcircuit named fracpole ready for
    inclusion into a spice file
    """
    slope_a, slope_b = param_cpe_slope(conc)
    pts, y_theta = get_cpeParams(fmin, fmax, m)

    out = ""
    out += "****************************************\n"
    out += "*           Fracpole/CPE start         *\n"
    out += "****************************************\n"

    fracpoleElements = []

    for point in pts:
        omega = 2 * math.pi * point
        R = slope_a * math.pow(point, slope_b)
        C = math.pow((R / (y_theta * R)), m) / (omega * R)
        fracpoleElements.append({'frequency': point, 'R': R, 'C': C})

    out += ".SUBCKT fracpole a b\n"
    for num, facpoleElement in enumerate(fracpoleElements):
        out += ("R" + str(num) + " a " + str(num + 1)
                           + " " + str(facpoleElement['R']) + "\n")
        out += ("C" + str(num) + " " + str(num + 1)
                           + " b " + str(facpoleElement['C']) + "\n")
    out += ".ENDS fracpole\n"
    out += "\n"

    return (out, 'fracpole')


def pbs_conductivity(conc):
    """
    Converts a concentration of PBS into a conductivity according to a
    least squares fit of the solutions used - fit code follows...
    """
    #==========================================================================
    # Linear relationship
    #==========================================================================
    m = 1.67296736e-02  # Determined from optimisation
    c = 8.54665149e-05  # Determined from optimisation
    return m * conc + c


def pbs_resistivity(conc):
    return 1 / pbs_conductivity(conc)


def generate_ladder(electrodes, margin, depth, Rr_electrode, Rv_commence):
    """
    Generates a resistor ladder circuit for insertion into a spice file.
    Parameters:
        electrodes:   Integer number of electrodes to create the ladder around.
        margin:       Integer number of dummy rows at each end of ladder (helps
                      to prevent end effects).
        depth:        How deep (column-wise) to generate the ladder.
        Rr_electrode: Radial resistance at electrode.
        Rv_commence:  Initial value of the vertical resistor.
    """
    # Derived from the value of Rr_insulator
    Rr_insulator = Rr_electrode * (3 / 4.0)

    # Populate the latitude resistor value array
    Rv = []
    for i in range(depth):
        Rv.append(float(Rv_commence) / pow(4, i))

    # Keep track of which nodes correspond to which electrodes
    nodes = {}

    # Generate the resistor ladder
    out = ""
    out += "****************************************\n"
    out += "*         Resistor ladder Start        *\n"
    out += "****************************************\n"
    out += ".SUBCKT resistorLadder"
    for electrode in range(electrodes):
        out += " e" + str((electrode + 1))
    out += "\n"

    # Figure out which nodes correspond to electrodes
    for row in range(((electrodes + electrodes - 1) * 2 - 1) + 4 * margin):
        for col in range(depth):
            if col == 0 and row % 2 == 0:
                actRow = row / 2
                if actRow < (margin + (electrodes * 2) - 1):
                    segment = (actRow - margin)
                    if segment % 2 == 0 and segment >= 0:
                        nodes[col + (int(row / 2) * 5) + 1] = (int(segment / 2)
                                                               + 1)

    # Step over each component adding as necessary
    for row in range(((electrodes + electrodes - 1) * 2 - 1) + 4 * margin):
        for col in range(depth):

            fromNode = col + (int(row / 2) * 5) + 1

            if (row % 2) == 0:
                if (row / 2 >= margin and
                    row / 2 < (margin + (electrodes * 2) - 1) and
                    (row / 2 - margin) % 2 != 0):
                    value = Rr_insulator
                else:
                    value = Rr_electrode

                component = "RRAD_" + str(row + 1) + "_" + str(col + 1)
                if col == (len(Rv) - 1):
                    toNode = 1000
                else:
                    toNode = col + (int(row / 2) * 5) + 2
            else:
                value = Rv[col]
                toNode = col + (int(row / 2 + 1) * 5) + 1
                component = "RVERT_" + str(row + 1) + "_" + str(col + 1)

            if fromNode in nodes:
                fromNode = 'e' + str(nodes[fromNode])

            if toNode in nodes:
                toNode = 'e' + str(nodes[toNode])
            out += (str(component) + ' ' +
                       str(fromNode) + ' ' +
                       str(toNode) + ' ' +
                       str(value) + "\n")

    out += ".ENDS resistorLadder\n"
    out += "\n"
    return (out, 'resistorLadder')


class Command(object):
    """
    Responsible for running a subprocess but with the ability to terminate
    that process if and when if executes for a pre-determined amount of time.
    """
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            with open(os.devnull, 'w') as dnull:
                self.process = subprocess.Popen(self.cmd,
                                                stdout=dnull,
                                                stderr=subprocess.STDOUT,
                                                shell=True)
            self.process.communicate()

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()
            return False
        else:
            return True


def simulate_spice(circuit,
                   filename=None,
                   outputName=None,
                   debug=False,
                   cleanup=False,
                   timeout=None):
    """
    Takes a string representing a spice circuit, saves it to a file,
    runs it through ngspice and returns the results as an array
    """
    global command

    # Sort out some defaults
    if filename is None:
        filename = 'spicemodel'
    if outputName is None:
        outputName = 'output_spice'

    outputName += '.data'
    filename += '_netlist.spice'

    filename = '../tmp/' + filename

    try:
        # Clean up temp files
        os.remove(filename)
        os.remove(outputName)
    except OSError:
        pass

    with open(filename, 'w') as f:
        f.write(circuit)

    # Run the simulation
    if debug == False:
        # This will use the timeout provided
        if command is None:
            command = Command("ngspice -bp " + filename)
        if command.run(timeout) == False:
            print "A errant simulation terminated"
            return None
    else:
        subprocess.call(["ngspice", "-bp", filename])

    # Fetch the results and place into an array
    data = None
    with open(outputName, 'r') as f:

        lines = f.readlines()
        for i, line in enumerate(lines):
            parts = [float(part) for part in line.split()]

            if data is None:
                data = np.zeros((len(parts), len(lines)))

            for j, part in enumerate(parts):
                data[j][i] = part

    # Clean up so the working directory doesnt get clogged up
    if cleanup:
        try:
            os.remove(filename)
            os.remove(outputName)
            print("Cleaned up temporary files")
        except OSError:
            pass

    return data


def get_defaultParams():
    return {'cm': 0.0002,  # Memristor responce capacitance
            'rm': 1500000,  # Memristor memory fade resistance
            'rs': 400  # Series resistance
            }