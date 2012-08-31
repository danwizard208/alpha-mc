#!/usr/bin/env python
import sys
import math
import ROOT
import io
from ROOT import TVector3

AV_radius = 6000 #mm
AV_inner_radius = 5999 #mm
counter_radius = 25.4 #mm
counter_height = math.sqrt((AV_inner_radius ** 2) - (counter_radius ** 2)) #mm

def scale(scalar, vector):
    """Scale vector by scalar"""
    return TVector3(scalar * vector.X(), scalar * vector.Y(), scalar * vector.Z())


ROOT.gROOT.ProcessLine('.x $RATROOT/rootinit.C')

# filename = sys.argv[1] if len(sys.argv) >= 2 \
#         else raw_input("File to process?")
filename = "alpha.root"
f = ROOT.TFile(filename)
Tree = f.Get('T');

total_hits = 0
for i in range(Tree.GetEntries()):
    Tree.GetEntry(i)
    rds = Tree.ds
    rmc = rds.GetMC()
    nav = TrackNav(rmc)
    cursor = nav.Cursor(True)
    # for j in range(rmc.GetMCTrackCount()):

print "Total hits: " + str(total_hits)
