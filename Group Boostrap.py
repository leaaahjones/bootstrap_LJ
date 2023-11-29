#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:40:30 2023

@author: leah
"""

import pandas as pd
from plotnine import *
import os
import numpy as np


os.chdir("/Users/leah/Desktop/2450 Spyder/Notes")
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat  = dat["Combined Mileage (mpg)"]


class Boot_CI():
    def __init__(self, data = None):
        "Initialize the simulation"
        self.stat = "mean"
        self.dat = data
        self.n_boot = 0 
        self.boot_stat = []
        self.ci_level = .95

        
    def add_sims(self):
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
        
    def set_statistic(self, stat):
        self.boot_stat = []
        self.stat = stat
        
    def plot_boot(self):
        boot_df = pd.DataFrame({'x': self.boot_stat})
    
        p = (
            ggplot(boot_df, aes(x='x')) +
            geom_histogram()
            )
    
        return p
        
    def conf_interval(self):
        if len(self.boot_stat) == 0:
            print("Boot_stat is 0. Must run sample first")
            
        else: 
            alpha = float(input("Please enter confidence level percentage: "))
            alpha = alpha/2
            np.percentile(self.boot_stat, [alpha, 100-alpha])
            #do we need to return?  np.percent
            
            
    


        
test = Boot_CI()
test.load_data(data = dat)
test.update_n_boot(10000)
test.add_sims()
test.plot_boot()


    

#######


    











