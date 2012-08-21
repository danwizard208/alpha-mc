#!/usr/bin/env python
import sys
import ROOT
import io

histo=ROOT.TH1F('transmit', "Transmitted energies", 100, .94E6, 1E6)
with open("TRANSMIT.txt") as transmit:
    for line in transmit:
        lines = line.split()
        if lines[0] == 'T':
            histo.Fill(float(lines[3]))

c = ROOT.TCanvas('c')
histo.Draw()
c.Draw()
raw_input("Enter to continue...")
