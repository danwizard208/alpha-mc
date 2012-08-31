#!/usr/bin/env python
import sys
import ROOT
import io

# Make a 1D histogram with 1000 bins, energy ranging spanning 5E6-7.7E6 ev
histo=ROOT.TH1F('transmit', "Transmitted energies", 1000, 5E6, 7.7E6)
with open("TRANSMIT.txt") as transmit:
    for line in transmit:
        lines = line.split() # Data lines are space separated fields
        if lines[0] == 'T': # Lines starting in 'T' are data lines
            histo.Fill(float(lines[3])) # Energy is 4th field (1st is 'T')

c = ROOT.TCanvas('c')
histo.Draw()
c.Draw()
raw_input("Enter to continue...")
