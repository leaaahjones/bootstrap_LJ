#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:40:30 2023

@author: leah
"""

import pandas as pd
from plotnine import *
import os

os.chdir("/Users/leah/Desktop/2450 Spyder/Notes")



class Boot_CI():
    def __init__(self):
        "Initialize the simulation"
        self.stat = "mean"
        self.dat = None
        self.n_boot = 0 
        self.boot_stat = None 
        self.ci_level = .95
        
        
        
    def for_loop(self):
        self.boot_stat = []
        for i in range(self.n_boot):
            boot_sample = self.dat.sample(n, replace = True)
            
            if self.stat == "median":
                self.boot_stat.append(float(boot_sample.median()))
                
            elif self.stat == "mean":
                self.boot_stat.append(float(boot_sample.mean()))
                
            elif self.stat == "std dev":
                self.boot_stat.append(float(boot_sample.std()))
                
            else: 
                raise TypeError("Wrong Statistic name")
                
    def clear_sims(self):
        self.boot_stat = []

        
    


test = Boot_CI(ci_level = .95)














