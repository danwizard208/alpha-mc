A simulation of the Alpha Counters in the AV
================================================================
The simulation comprises two main stages:

*   RAT generates the initial event positions, energies, and directions
*   SRIM calculates the final energies of events reaching the counters

Running the simulation is a rather convoluted process,
requiring separate invocations of python, RAT, and SRIM.
The net result will be a plot of the energy spectrum generated.

Requirements
------------
*   A linux installation with RAT and PyROOT
*   A windows installation with SRIM

This repository should be installed on your RAT enabled linux installation.

Setting up
----------
1.  Clone this repository on your linux installation.
2.  Copy the file "alphacounter.geo" to the "data/geo" directory of RAT.
3.  Edit number in the file "TRIMAUTO" to 1 (this tells TRIM to run in batch mode)

Running the Simulation
----------------------
0.  Start in this repository.
1.  Run rat on the file "generate\_events.mac" (`# rat generate_events.mac`)
2.  Run the script "process\_events.py" (`# ./process_events.py`)
3.  Copy the file "TRIM.DAT" to the SRIM directory on your windows installation,
    overriding an already existing file if necessary.
4.  Copy the "TRIM.IN" file corresponding to the material you are using to the
    SRIM directory, overriding if necessary.
5.  Run "TRIM.EXE".
6.  A file TRANSMIT.txt will be generated in SRIM - Outputs - 
    copy this to this repository on your linux installation.
7.  Run the script "final\_histo.py" (`# ./final_histo.py`)
8.  Marvel at the plot!

Tweaking Parameters
-------------------
There are a number of parameters for the simulation that you can tweak,
located across various various files used in the simulation process.
Each file and parameter is described in the file "parameters-files".

Essentially, to edit a parameter,
just replace the value in the corresponding file.
compute-parameters.py can be used to generate the geometry values,
and TIN.EXE (in SRIM) can be used to generate the TRIM.IN files.

The Simulation Pipeline
-----------------------
As you may have noticed, this simulation involves chaining a bunch of
procesess together, where each process reads data in, and spits data out.
For this reason, I like to think of the whole process as a pipeline,
though there is at the moment no actual piping involved.
Anyway, here is a full description of how this simulation works:

1.  RAT uses generate\_events.mac and alphacounter.geo to generate the
    initial events, depositing them in alpha.root.
2.  process\_events.py reads alpha.root, calculates which events have
    trajectories that intersect the counter, and creates TRIM input data
    for those events, stored in TRIM.DAT.
3.  TRIM runs in batch-mode, reading in TRIM.DAT and TRIM.IN 
    (which specifies the properties of the material the particles travel
    through, in our case Air and Nitrogen), and generating the final
    kinetics in TRANSMIT.txt
4.  final\_histo.py reads in TRANSMIT.txt and uses it to make a plot
    of the resulting energy spectrum.
