#!/usr/bin/env python
import sys
import math

AV_radius = 6000.0 #milimetres
AV_inner_radius = 5999.0 #milimetres
counter_radius = float(sys.argv[1]) if len(sys.argv) >=2 \
        else float(raw_input("Counter radius (in milimetres)?"))
counter_height = AV_inner_radius - math.sqrt(AV_inner_radius**2 - counter_radius**2)
phi = math.degrees(math.asin(counter_radius/AV_inner_radius))

print "Phi is: " + str(phi)
print "Height is " + str(counter_height)
