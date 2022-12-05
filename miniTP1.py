# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:36:20 2022

@author: sylva
"""

import os
import sys

liste = os.listdir(sys.argv[1])

for nb,i in enumerate(liste):
    print(f"{nb}. {i}")
    
print(liste)