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
TODO

Running the Simulation
----------------------
This is the procedure to rerun the simulation from scratch, 
without adjusting any parameters:

0.  Start in this repository.
1.  Run rat on the file "generate\_events.mac" (`# rat generate_events.mac`)
2.  Run the script "process\_events.py" (`# ./process_events.py`)
3.  Copy the file "TRIM.DAT" to the SRIM directory on your windows installation,
    overriding an already existing file if necessary.
4.  Launch SRIM, and choose to run TRIM.
5.  If you've already run a simulation, you should be able to just select
    "Restore Last TRIM Data", then "Save Input and Run TRIM".
    You'll have to click through a couple of dialog boxes.
6.  If you haven't yet run a simulation, you'll have to manually specify
    fill in this form. See below for how.
7.  Once TRIM is done running, allow it to save, then exit,
    allowing it to save again.
8.  A file TRANSMIT.txt will be generated in SRIM - Outputs - 
    copy this to this repository on your linux installation.
9.  Run the script "final\_histo.py" (`# ./final_histo.py`)
10. Marvel at the plot!

Tweaking Parameters
-------------------
TODO
