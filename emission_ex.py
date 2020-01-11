#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 06:23:52 2020

@author: davidhampton
"""

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data into dataframe
df = pd.read_csv('API_EN_ATM_CO2E_PC_DS2_en_csv_v2_566534.csv') 
#characterize data
df.head(4)
df.describe()
df.info()

#make dataframe with only numbers
df_nums = df.iloc[:,4:59]


#Plot mean & quantiles
plt.figure();

df.mean().plot(kind='line', color='k', linewidth=4)
df_nums.min().plot(kind='line')
df_nums.quantile(0.25).plot(kind='line')
df.median().plot(kind='line')
df_nums.quantile(0.75).plot(kind='line')
df_nums.quantile(0.90).plot(kind='line')

plt.title('Mean closer to 75th than 50th')
plt.xlabel('$Year')
plt.ylabel('$CO_2$ metric tons/capita')
plt.xlabel('Year')
labels = ['mean', '0th', '25th', '50th', '75th', '90th']
plt.legend(labels)
plt.savefig('Mean_quantiles.png')


#Plot upper quantiles
plt.figure();

df_nums.quantile(0.90).plot(kind='line')
df_nums.quantile(0.91).plot(kind='line')
df_nums.quantile(0.92).plot(kind='line')
df_nums.quantile(0.93).plot(kind='line')
df_nums.quantile(0.94).plot(kind='line')
df_nums.quantile(0.95).plot(kind='line')
df_nums.quantile(0.96).plot(kind='line')
df_nums.quantile(0.97).plot(kind='line')
df_nums.quantile(0.98).plot(kind='line')
df_nums.quantile(0.99).plot(kind='line')
df_nums.max().plot(kind='line')

plt.title('Top 98th disproportionately large')
plt.ylabel('$CO_2$ metric tons/capita')
plt.xlabel('Year')
labels = ['90th', '91st', '92nd', '93rd', '94th', '95th', '96th', '97th', \
          '98th', '99th', '100th']
plt.legend(labels)
plt.savefig('Upper_quantiles.png')


#Plot year by country
plt.figure();
df_nums.plot(kind='line')

plt.title('Few super offenders')
plt.ylabel('$CO_2$ metric tons/capita')
plt.xlabel('Country #')
plt.savefig('CO2_country.png')


#Dataframe to array           
A = df_nums.to_numpy()
yearly_change = A[:,1:55] - A[:,0:54]
#Plot mean change/year
plt.figure();
plt.plot(np.arange(1961, 2015), np.nanmean(yearly_change, axis = 0))
plt.plot(np.arange(1961, 2015), np.zeros(54), '--', color='k')
change = str(round(np.nanmean(yearly_change), 3))
avg_change = str(round(np.nanmean(yearly_change)*54, 2))

plt.title('Avg/year = ' + change + ' x 54 yrs = ' +  avg_change)
plt.ylabel('Change in $CO_2$ metric tons/capita')
plt.xlabel('Year')
plt.savefig('Yearly_change.png')


#Find number of countries in 90th percentile range
country_num = len(A)
country_num
top_90th_year_country = np.where( A > 8 )
top_90th_country = np.unique(top_90th_year_country[0])
top_90th_country_num = top_90th_country.size
top_90th_country_num
top_90th_country_num/country_num

#Find number of countries in 98th percentile range
top_97th_year_country = np.where( A > 20 )
top_97th_country = np.unique(top_97th_year_country[0])
top_97th_country_num = top_97th_country.size
top_97th_country_num
top_97th_country_num/country_num

#Dataframe from super offenders
df_97 = df.iloc[top_97th_country,np.arange(4, 59)]
#Array of super offenders
A_97 = df_97.to_numpy()
#Dataframe of super offender names
names_97 = df.iloc[top_97th_country,0]
#Array of super offender names
A_97_names = names_97.to_numpy()


#Plot super offenders by year
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(np.arange(1960, 2015), np.transpose(A_97))

# Shrink current axis by 30% to include legend
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])

# Put a legend to the right of the current axis
ax.legend(A_97_names, loc='center left', bbox_to_anchor=(1, 0.5))

plt.title('Super offenders')
plt.ylabel('Change in $CO_2$ metric tons/capita')
plt.xlabel('Year')
plt.savefig('Super_Offenders.png')













