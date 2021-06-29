#!/usr/bin/env python3
# File              : test_diffusion_map.py
# Author            : George Arampatzis <garampat@ethz.ch>
# Date              : 29.06.2021
# Last Modified Date: 29.06.2021
# Last Modified By  : George Arampatzis <garampat@ethz.ch>
"""
Validation of the diffusion_map module with the results from 
the matlab script testOperators.m in
https://github.com/sandstede-lab/eq-free
"""
import numpy as np
from  diffusion_map import *

with open('data/alignData_small.csv') as f:
  data =  np.loadtxt(f, delimiter=",")

# Create a diffusion map object using the loaded data
dm = DiffusionMap(data,1,5)

# Compute the restriction error
(percentError, restricted, restictDiff) = dm.testRestrict()
print( f'Error in the restriction: {np.mean(percentError)} ')

# Compute the lift error
(percentError, restricted, restictDiff) = dm.testLift(3)
print(f'Erron in the lift: {np.mean(percentError)}')
