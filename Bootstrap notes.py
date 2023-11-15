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

dat = pd.DataFrame({"handspan": [20, 20, 19, 24.2, 20, 20.2, 21.5, 17, 19.5, 
            21.6, 18, 18, 20.5, 20, 20.3, 21.5, 19, 20.4, 
            22.7, 22.9, 15, 23, 23.8, 22, 21.5, 21.5]})



boot_sample = dat.sample(26, replace = True)
boot_sample.mean()



boot_means = []

for i in range(10_000):
    boot_sample = dat.sample(26, replace = True)
    boot_means.append(float(boot_sample.mean()))



boot_df = pd.DataFrame({'x' : boot_means})


#make histogram
(
 ggplot(boot_df, aes(x = 'x')) +
 geom_histogram()
)




## create a loop you get to choose sampling distr from 
stat = "mean"

boot_stat = []
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat  = dat["Combined Mileage (mpg)"]
n = len(variable)
n_boot = 10_000

for i in range(n_boot):
    boot_sample = dat.sample(n, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
        
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
        
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
        
    else: 
        raise TypeError("Wrong Statistic name")



boot_df = pd.DataFrame({'x' : boot_stat})


#make histogram
(
 ggplot(boot_df, aes(x = 'x')) +
 geom_histogram()
)



## reading in car data 


























