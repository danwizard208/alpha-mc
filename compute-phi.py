#!/usr/bin/env python
import sys
import math

AV_RADIUS = 6000.0 #milimetres

counter_radius = float(sys.argv[1]) if len(sys.argv) >=2 \
        else float(raw_input("Counter radius (in milimetres)?"))

phi = math.degrees(math.asin(counter_radius/AV_RADIUS))

print phi
