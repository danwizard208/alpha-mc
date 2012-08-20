#!/usr/bin/env python
import sys
import math
import ROOT
import io
from ROOT import TVector3

AV_radius = 6000 #mm
AV_inner_radius = 5999 #mm
counter_radius = 10 #mm
counter_height = math.sqrt((AV_inner_radius ** 2) - (counter_radius ** 2)) #mm

def scale(scalar, vector):
    """Scale vector by scalar"""
    return TVector3(scalar * vector.X(), scalar * vector.Y(), scalar * vector.Z())

def data_line(name, pos, mom, ke):
    """Make a trim data line from the event data
    
    TRIM expects a line containing a string, an int, and 7 floats,
    separated by whitespace.
    
    Function takes in name, a 5-char string; pos, a position vector in mm;
    mom, a momentum vector in MeV/c; and ke, kinetic energy in MeV."""

    # For simplicity in generating events, they were centred on the north pole.
    # But TRIM fires particles along X axis, so we rotate around Y axis.
    # TRIM also starts at the origin, so subtract x from radius of AV 
    x = AV_inner_radius - pos.Z()
    y = pos.Y()
    z = pos.X()

    #TRIM takes directions in directional cosines
    cosx = - (mom.Z()/mom.Mag())
    cosy = mom.Y()/mom.Mag()
    cosz = mom.X()/mom.Mag()

    line = ""
    # Name (string of five non-whitespace chars)
    line += " " + str(name) + " "
    # Atomic Number (always 4 for an alhpa particle)
    line += " 4 "
    # Kinetic Energy in ev
    line += " " + str(ke * 10**6) + " "

    # Depth in angstroms (angstroms/mm = 10^7)
    line += " " + str(x * 10**7) + " "
    # Y in angstroms (angstroms/mm = 10^7)
    line += " " + str(y * 10**7) + " "
    # Z in angstroms (angstroms/mm = 10^7)
    line += " " + str(z * 10**7) + " "

    # Cos(X)
    line += " " + str(cosx) + " "
    # Cos(Y)
    line += " " + str(cosy) + " "
    # Cos(Z)
    line += " " + str(cosz) + " "

    return line


ROOT.gROOT.ProcessLine('.x $RATROOT/rootinit.C')

# filename = sys.argv[1] if len(sys.argv) >= 2 \
#         else raw_input("File to process?")
filename = "alpha.root"
f = ROOT.TFile(filename)
Tree = f.Get('T');

with open("TRIM.DAT", 'w') as trimdat:
    total_hits = 0
    for i in range(Tree.GetEntries()):
        Tree.GetEntry(i)
        rds = Tree.ds
        rmc = rds.GetMC()
        for j in range(rmc.GetMCParticleCount()):
            rmcparticle = rmc.GetMCParticle(j)
            pos = rmcparticle.GetPos() #position in mm
            mom = rmcparticle.GetMom() #momentum in MeV/c
            ke = rmcparticle.GetKE() #KE in MeV
            # Scale pos to AV_inner_radius:
            # hack to generate events only on the surface of the acrylic.
            pos = scale(AV_inner_radius / pos.Mag(), pos)
            # Time it would take the particle to reach the counter's height
            # (Units are (c * mm)/MeV, dimensions of T/M; irrelevant here)
            t = (counter_height - pos.Z()) / mom.Z() 
            if t < 0: 
                continue #Negative time means it will never reach counter
            final_pos = pos + (scale(t, mom))
            if (final_pos.X() ** 2 + final_pos.Y() ** 2) > counter_radius ** 2:
                continue #When it reaches the counter height, it's outside the radius
            # Trajectory lines up, now for SRIM stuff
            trimdat.write(data_line(str(i), pos, mom, ke)+'\r\n')

            # Print a hit, and increment hit count
            print "Particle number " + str(i) + " hits."
            total_hits+=1

print "Total hits: " + str(total_hits)
