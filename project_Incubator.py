#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:05:26 2020

@author: sarvenaz
"""

import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

df1 = pd.read_csv('energy_dataset.csv') # energy data 
df2 = pd.read_csv('weather_features.csv') # weather data
df2.rename(columns = {'dt_iso':'time'}, inplace = True) # renaming column's name on weather dataset
df = df1.merge(df2, how='inner', on='time') # Merging two data sets (energy and weather features)
col = list(df1.columns) # list of columns
# dropping rows in any of the time, total load actual or price actual
df.dropna(subset = ['time','total load actual','price actual'], how = 'any', inplace = True) 
df.head()


def init_plot(**kwargs):
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = kwargs.get('fontsize', 16)

    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['xtick.major.width'] = 2
    plt.rcParams['xtick.major.size'] = 4
    plt.rcParams['xtick.direction'] = 'in'


    plt.rcParams['ytick.labelsize'] = 14
    plt.rcParams['ytick.major.width'] = 2
    plt.rcParams['ytick.major.size'] = 4
    plt.rcParams['ytick.direction'] = 'in'


    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['axes.labelweight'] = 'normal'
    plt.rcParams['axes.titleweight'] = 'normal'
    plt.rcParams['legend.fontsize'] = 14
    plt.rcParams['mathtext.default'] ='regular'
    
    # convert string date and time to datetime
df['time'] = df['time'].apply(lambda x : pd.to_datetime(str(x), utc = True).tz_convert('UTC')) 
#init_plot()
plt.figure(figsize=(13,7))
colors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0,0,0]]
months = [1]
count = -1

for month in months:
    df_xdata = pd.DataFrame()
    df_ydata_load = pd.DataFrame()
    df_ydata_price = pd.DataFrame()
    offset = 0;
    count += 1 
    for i in [1]: # masking over days of the first week on January
        mask = (df['time'].dt.year == 2015) & (df['time'].dt.month == month) & (df['time'].dt.day == i);
        df_masked = df.loc[mask] 
        df_cur_hour = df_masked['time'].dt.hour
        df_cur_hour += offset 
        df_xdata = pd.concat([df_xdata, df_cur_hour], axis = 0)
        offset += 24 
        df_ydata_load = pd.concat([df_ydata_load, df_masked['total load actual']], axis=0)#concatinating the total load actual values
        df_ydata_price = pd.concat([df_ydata_price, df_masked['price actual']], axis=0)# concatinating the price actual values
        ax1 = plt.subplot(211)
        plt.plot(df_xdata, df_ydata_load, color = colors[count], lw = 1.5)
        ax2 = plt.subplot(212)
        plt.plot(df_xdata, df_ydata_price, color = colors[count], lw = 1.5)


ax1.set_ylabel('Load (MW)')
ax2.set_ylabel('Price ($)')
ax1.set_xlabel('Hour of week (H)')
ax2.set_xlabel('Hour of week (H)')
plt.savefig('loadpricevshour.pdf')
plt.show()
#ax.legend([''],loc='upper center', bbox_to_anchor=(0.5, -0.05),
#          fancybox=True, ncol=4 )

