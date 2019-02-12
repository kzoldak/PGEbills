#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:21:57 2019

@author: kimzoldak
"""

direc = '/Users/kimzoldak/Github/PGEbills/'
import os
os.chdir(direc)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'data/weatherdata.csv'
weather = pd.read_csv(filename)

#weather.DATE.astype(pd.datetime)
#weather.DATE = weather.DATE.astype(pd.datetime)

weather['DATE'] = pd.to_datetime(weather.DATE)


#weather.dropna()

# REMOVE ALL LAFAYETTE ENTRIES, THEY DON'T HAVE TEMPERATURES.
boolean = weather.NAME.str.contains('LAFAYETTE')
weather = weather[~boolean]

# CHECKING TO SEE HOW MANY DUPLICAES DATES THERE ARE
sum(weather.DATE.value_counts() < 2)  # 0
sum(weather.DATE.value_counts() > 2)  # 0

# CHECK TO SEE IF ANY TAVG ARE NANS
weather.TAVG.isna().sum()  # 0
# CHECK MIN AND MAX TEMPS TOO
weather.TMIN.isna().sum()  # 0
weather.TMAX.isna().sum()  # 0





# TAVG is the average temperatures.
# AVERAGE BBRIONES AND LAS TRAMPAS TOGETHER:
daily_avg_temps = weather.groupby('DATE').TAVG.mean()

daily_min_temps = weather.groupby('DATE').TMIN.mean()

daily_max_temps = weather.groupby('DATE').TMAX.mean()

'''
Treat the min and max temperatures as if they were errorbars. 
'''





'''
There are two reports per day. One from Las Trampas and one from Briones. 
Lets average their average temperatures. 
'''

plt.rcParams['figure.figsize'] = [8, 8/1.5] # [6.0, 4.0] is default


 
    
    
#    PLT = ax.plot(x, y, color='red', linestyle='--', 
#                  lw=2, alpha=0.6)
#    ax.xticks(rotation=60)
#    #xticks(np.arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'))
#    return PLT



bill_cycles = [['2018-10-05','2018-11-05'], 
               ['2018-11-06','2018-12-05'], 
               ['2018-12-06','2019-01-06'],
               ['2019-01-07','2019-02-05']]


daily_avg_temps.loc['2018-10-05':'2018-11-05']

daily_avg_temps.loc['2018-11-06':'2018-12-05']

daily_avg_temps.loc['2018-12-06':'2019-01-06']

daily_avg_temps.loc['2019-01-07':'2019-02-05']


daily_avg_temps.loc['2018-10-05':'2018-11-05'].plot()


xdata = daily_avg_temps.loc['2018-10-05':'2018-11-05'].index
ydata = daily_avg_temps.loc['2018-10-05':'2018-11-05']


plot_average_temps(xdata, ydata)

daily_avg_temps.between_time(start_time ='2018-11-06',
                             end_time='2018-12-05')



keys = plt.rcParams.keys()


weather.groupby('DATE')


#fig,ax = plt.subplot()

locs = []
for i in daily_avg_temps.index:
    if i.day in [1, 15]:
        locs.append(i)
        #print(i)
    

bill_cycles = [['2018-10-05','2018-11-05'], 
               ['2018-11-06','2018-12-05'], 
               ['2018-12-06','2019-01-06'],
               ['2019-01-07','2019-02-05']]





def plot_average_temps(xdata, ydata, ax=None):
    if ax is None:
        ax = plt.gca()
    x,y = xdata,ydata
    
    #plt.figure(figsize=(15,7))
    x,y = xdata,ydata
    PLT = ax.plot(x, y, color='red', linestyle='--', 
                  lw=2, alpha=0.6)
    ax.text(0.2, 0.95, 'mean temp: %i$\degree$F'%y.mean(),
            fontsize = 18,
            horizontalalignment='center',
            verticalalignment='center', 
            transform=ax.transAxes)
    #ax.figtext(0.2, 0.9, 'mean temp: %i'%y.mean(),
    #            fontsize=18)
    #ax.set_xticks(rotation=10)
    ax.tick_params(axis='x', labelrotation=10)
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(20, 75)
    #plt.show()
    return PLT
   
    

for bill in bill_cycles:
    xdata = daily_avg_temps.loc[bill[0]:bill[1]].index
    ydata = daily_avg_temps.loc[bill[0]:bill[1]]

    plt.figure(figsize=(15,7))
    plot_average_temps(xdata, ydata)
    plt.show()
    
    
    
    
ax.ticklabel_format(*, axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    
 
ax.tick_params(aix='x', labelrotation=10)
   
#    #x,y = daily_avg_temps.index, daily_avg_temps
#    x,y = xdata,ydata
#    plt.plot(x, y, color='red', linestyle='--', 
#                  lw=2, alpha=0.6)
#    plt.figtext(0.2, 0.9, 'mean temp: %i'%y.mean(),
#                fontsize=18)
#    plt.xticks(rotation=10)
#    plt.xlim(x.min(), x.max())
#    plt.ylim(20, 75)
#    plt.show()







#for bill in bill_cycles:
#    xdata = daily_avg_temps.loc[bill[0]:bill[1]].index
#    ydata = daily_avg_temps.loc[bill[0]:bill[1]]
#
#    plt.figure(figsize=(15,7))    
#    #x,y = daily_avg_temps.index, daily_avg_temps
#    x,y = xdata,ydata
#    plt.plot(x, y, color='red', linestyle='--', 
#                  lw=2, alpha=0.6)
#    plt.figtext(0.2, 0.9, 'mean temp: %i'%y.mean(),
#                fontsize=18)
#    plt.xticks(rotation=10)
#    plt.xlim(x.min(), x.max())
#    plt.ylim(20, 75)
#    plt.show()

