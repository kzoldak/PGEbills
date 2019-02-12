#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:02:14 2019

@author: kimzoldak
"""

direc = '/Users/kimzoldak/Github/PGEbills/'
import os
os.chdir(direc)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



filename = 'data/pge_electric_interval_data__2018-10-04_to_2019-02-11.csv'
pge = pd.read_csv(filename, skiprows=5)

# FIX COLUMN NAMES - REPLACE WHITESPACE
pge.columns = pge.columns.str.replace(' ', '_')

pge['DATE'] = pd.to_datetime(pge.DATE)
pge['START_TIME'] = pd.to_datetime(pge.START_TIME)
pge['END_TIME'] = pd.to_datetime(pge.END_TIME)


pge.groupby('DATE').USAGE.sum()

bill_cycles = [['2018-10-05','2018-11-05'], 
               ['2018-11-06','2018-12-05'], 
               ['2018-12-06','2019-01-06'],
               ['2019-01-07','2019-02-05']]






for bill in bill_cycles:
    xdata = pge.groupby('DATE').USAGE.sum().loc[bill[0]:bill[1]].index
    ydata = pge.groupby('DATE').USAGE.sum().loc[bill[0]:bill[1]]
    #xdata = daily_avg_temps.loc[bill[0]:bill[1]].index
    #ydata = daily_avg_temps.loc[bill[0]:bill[1]]

    plt.figure(figsize=(15,7))    
    #x,y = daily_avg_temps.index, daily_avg_temps
    x,y = xdata,ydata
    plt.hist(x, bins=len(x))
#    plt.plot(x, y, color='blue', marker='o',
#             #linestyle='--', 
#             lw=0, alpha=1)
    plt.figtext(0.2, 0.9, 'mean usage: %i'%y.mean(),
                fontsize=18)
    plt.xticks(rotation=10)
    plt.xlim(x.min(), x.max())
    #plt.ylim(20, 75)
    plt.show()






def plot_average_usage(xdata, ydata, ax=None):
    if ax is None:
        ax = plt.gca()
    x,y = xdata,ydata

    PLT = ax.bar(x=x, height=y, align='center', 
                 color='blue', alpha=0.5)
    ax.text(0.2, 0.95, 'mean usage: %.1f kWh'%y.mean(),
            fontsize = 18,
            horizontalalignment='center',
            verticalalignment='center', 
            transform=ax.transAxes)
        
    #plt.figtext(0.2, 0.9, 'mean usage: %i'%y.mean(),
    #            fontsize=18)
    ax.set_xticks(rotation=10)
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(0, 55)
    return PLT
    
    



plt.clf()
for bill in bill_cycles:
    plt.figure(figsize=(15,7))  
    xdata = pge.groupby('DATE').USAGE.sum().loc[bill[0]:bill[1]].index
    ydata = pge.groupby('DATE').USAGE.sum().loc[bill[0]:bill[1]]
    plot_average_usage(xdata, ydata)
    plt.show()
    
    


plt.clf()
for bill in bill_cycles:
    xdata = pge.groupby('DATE').USAGE.sum().loc[bill[0]:bill[1]].index
    ydata = pge.groupby('DATE').USAGE.sum().loc[bill[0]:bill[1]]
    
    plt.figure(figsize=(15,7))    
    x,y = xdata,ydata
    plt.bar(x=x, height=y, align='center', alpha=0.5)
    plt.figtext(0.2, 0.9, 'mean usage: %i'%y.mean(),
                fontsize=18)
    plt.xticks(rotation=10)
    plt.xlim(x.min(), x.max())
    plt.ylim(0, 55)
    plt.show()



    