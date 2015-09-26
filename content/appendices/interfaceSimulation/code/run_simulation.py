# Custom libraries
import lib_functions
import lib_simulate

# Math helpers
import numpy as np
import mpmath

def simulate_model(conc=None,
                   measurements=None,
                   params=None,
                   res=0.1):
    """Runs the model and returns the results as a numpy array -
        pass the solution concentration."""
    #=========================================================================
    # Set basic simulation parameters
    #=========================================================================
    fmin = 20e-3  # Set frequency bandwidth for CPE building
    fmax = 1e5


    cond = lib_simulate.pbs_conductivity(conc)
    electrodes = 8

    #=========================================================================
    # Build spice circuit simulation components
    #=========================================================================
    Rr, Rv = lib_simulate.ladderResistorValues(cond)

    ladderSubckt, ladderName = lib_simulate.generate_ladder(electrodes=electrodes,
                                                            margin=3,
                                                            depth=5,
                                                            Rr_electrode=Rr,
                                                            Rv_commence=Rv)

    if params is None:
        params = lib_simulate.get_defaultParams()
        print("No params passed - DEFAULTS WILL BE USED!")

    fracpoleSubckt, fracpoleName = lib_simulate.generate_fracpoleSubcircuit(conc,
                                                                            fmin,
                                                                            fmax)

    #=========================================================================
    # Define the measurement points
    #=========================================================================
    if measurements is None:
        measurements = [('v_mag', 'VR(input,el6)'),
                        ('v_phi', 'VI(input,el6)'),
                        ('current', 'i(V1)')]

    #=========================================================================
    # Build the spice file
    #=========================================================================
    spice_ckt = "circuit\n"
    spice_ckt += ladderSubckt
    spice_ckt += fracpoleSubckt
    spice_ckt += ".SUBCKT interface a b\n"
    spice_ckt += "X1 a mid fracpole\n"
    spice_ckt += "Rs mid b " + str(params['rs']) + "\n"
    spice_ckt += ".ENDS interface\n"
    spice_ckt += "\n"
    spice_ckt += "****************************************\n"
    spice_ckt += "*          Circuit description         *\n"
    spice_ckt += "****************************************\n"
    spice_ckt += "XLadder el1 el2 el3 el4 el5 el6 el7 el8 resistorLadder\n"
    spice_ckt += "\n* Interface models from (Water to Electrode)\n"
    spice_ckt += "XInterface2 em2 el2 interface\n"
    spice_ckt += "XInterface7 em7 el7 interface\n"
    spice_ckt += "\n* Connections to power\n"
    spice_ckt += "R_IN input em7 0\n"
    spice_ckt += "R_OUT 0 em2 0\n"
    spice_ckt += "\n"
    spice_ckt += "\n* Power supply\n"
    spice_ckt += "V1 input 0 0 AC 1\n"
    spice_ckt += "\n"
    spice_ckt += "****************************************\n"
    spice_ckt += "*           Simulation options         *\n"
    spice_ckt += "****************************************\n"
    spice_ckt += ".control\n"
    spice_ckt += "set appendwrite\n"
    spice_ckt += "AC DEC 10 0.05 10000\n"
    spice_ckt += "wrdata output_spice "
    for measurement in measurements:
        spice_ckt += measurement[1] + ' '
    spice_ckt += "\n"
    spice_ckt += ".endc\n"
    spice_ckt += ".END"
    #=========================================================================
    # Simulate the circuit and return the results
    #=========================================================================
    simulation = lib_simulate.simulate_spice(spice_ckt)


    voltages = map(lambda (r, i): mpmath.mpc(r, i), zip(simulation[1], simulation[3]))
    currents = map(lambda (r, i): mpmath.mpc(r, i), zip(simulation[5], simulation[6]))
    data = np.array(zip(simulation[0],
                        voltages,
                        currents),
                        dtype={'names':('frequency',
                                        'voltage',
                                        'current'),
                               'formats':('f', 'complex', 'complex')})
    return data


# Simulate a solution of 0.5X PBS
concentration = 0.5
result = simulate_model(concentration)

# Print the results
for frequency in result['frequency']:
    print(result['frequency'], result['voltage'], result['current'])
