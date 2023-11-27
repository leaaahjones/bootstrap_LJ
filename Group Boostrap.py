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
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat  = dat["Combined Mileage (mpg)"]


class Boot_CI():
    def __init__(self, data = None):
        "Initialize the simulation"
        self.stat = "mean"
        self.dat = data
        self.n_boot = 0 
        self.boot_stat = None 
        self.ci_level = .95
        
        
    def add_sims(self):
        self.boot_stat = []
        n = len(self.dat)
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
        
    def load_data(self,data):
        self.dat = data
        
    def update_n_boot(self, new_n_boot):
        self.n_boot = new_n_boot


        
test = Boot_CI()

test.load_data(data = dat)












