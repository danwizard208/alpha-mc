#!/usr/bin/env python
import sys
import math
import ROOT
from ROOT import TVector3

def scale(scalar, vector):
    """Scale vector by scalar"""
    return TVector3(scalar * vector.X(), scalar * vector.Y(), scalar * vector.Z())

ROOT.gROOT.ProcessLine('.x $RATROOT/rootinit.C')

# filename = sys.argv[1] if len(sys.argv) >= 2 \
#         else raw_input("File to process?")
filename = "alpha.root"
f = ROOT.TFile(filename)
Tree = f.Get('T');

AV_radius = 6000
counter_radius = 10
counter_height = math.sqrt((AV_radius ** 2) - (counter_radius ** 2))
total_hits = 0
for i in range(Tree.GetEntries()):
    Tree.GetEntry(i)
    rds = Tree.ds
    rmc = rds.GetMC()
    for j in range(rmc.GetMCParticleCount()):
        rmcparticle = rmc.GetMCParticle(j)
        pos = rmcparticle.GetPos()
        mom = rmcparticle.GetMom()
        # Time it would take the particle to reach the counter's height
        t = (counter_height - pos.Z()) / mom.Z() 
        if t < 0: 
            continue #Negative time means it will never reach counter
        final_pos = pos + (scale(t, mom))
        if (final_pos.X() ** 2 + final_pos.Y() ** 2) > counter_radius ** 2:
            continue #When it reaches the counter height, it's outside the radius
        # Trajectory lines up, now for SRIM stuff

        # In the meantime, let's just print a hit
        print "Particle number " + str(i) + 
        " hits with phi of " + str(mom.Phi())
        total_hits+=1

print "Total hits: " + str(total_hits)
