#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# plot actogram
root_path="root_path"
dir_list = os.listdir(root_path)
data_point_number=48*60*60/15
days=3
row_number=days*24*60*60/15
for file in dir_list:
    mouse=file[0:-5]
    print(mouse)
    sheet_name=file[0:-10]
    xls = pd.ExcelFile(root_path+mouse+'.xlsx')
    df1 = pd.read_excel(xls, sheet_name,skiprows=29)

    lost_row_number=df1.shape[0]
    new_row = {'Time':'00/00/0000 00:00:00', 'Activity':0.0}
    for i in range(lost_row_number+1):
        df1 = df1.append(new_row, ignore_index=True)
        

    fig, axs = plt.subplots(days,figsize=(20, 3))
    
    for day in range(0,days):
        
        axs[day].plot(df1.loc[day*24*60*60/15:(day+2)*24*60*60/15]['Activity'],color='black')
        axs[day].set_ylim(0,5)
        axs[day].get_yaxis().set_visible(True)
        axs[day].get_xaxis().set_visible(True)
        x_interval=np.arange(day*24*60*60/15,(day+2)*24*60*60/15+1,2*60*60/15)
    
        selected=df1.loc[x_interval]['Time'].tolist()
    
        
        timeticks=[]
        for a in selected:
            b=a[12:17]
            timeticks.append(b)
        
    plt.xticks(x_interval, timeticks)
    plt.savefig(root_path+sheet_name+"full.png")
    plt.show()

    
#calculate activity
root_path="/Users/xiangning/OneDrive - Johns Hopkins/Lab/monitor data/20230130/files/"
dir_list = os.listdir(root_path)
dir_list

mouse=dir_list[0][0:-5]

sheet_name=dir_list[0][0:-10]
xls = pd.ExcelFile(root_path+mouse+'.xlsx')
df1 = pd.read_excel(xls, sheet_name,skiprows=29)


FileStartDay=1
FileStartHour=12
FileStartMinute=14
FileStartSecond=55
interval=15
StartTime=(FileStartHour*60+FileStartMinute)*60+FileStartSecond

All_QuantDay=[2,2,2,2,2,2,2,2,2]
All_QuantHour=[14,13,14,17,11,12,12,14,17]
All_QuantMinute=[0,0,0,30,30,0,30,17,0]
All_QuantSecond=[0,0,0,0,0,0,0,0,0]


FinalSumActivity=[]
FinalPhase1Per=[]
for file,QuantDay,QuantHour,QuantMinute,QuantSecond in zip(dir_list,All_QuantDay,All_QuantHour,All_QuantMinute,All_QuantSecond):
    mouse=file[0:-5]
    print(mouse)
    sheet_name=file[0:-10]
    xls = pd.ExcelFile(root_path+mouse+'.xlsx')
    df1 = pd.read_excel(xls, sheet_name,skiprows=29)
    Allsum=[]
    Allphase1_activity_per=[]
    for day in range(0,3):
        print(day)
        startday=QuantDay+day
        Startline=round(((QuantHour*60+QuantMinute)*60+QuantSecond+startday*24*60*60-StartTime)/15)
        n=int(24*60*60/15)
        print(Startline)
        df2=df1.iloc[Startline:(Startline+n)]
        Sum_activity=df2['Activity'].sum()
        Allsum.append(Sum_activity)
        
        phase1=df1.iloc[Startline:(Startline+int(n/2))]
        phase1_activity=phase1['Activity'].sum()
        phase1_per=phase1_activity/Sum_activity
        Allphase1_activity_per.append(phase1_per)
        plt.plot(df2['Activity'])
        plt.show()
        plt.plot(df2['Activity'].cumsum())
        plt.show()
    FinalSumActivity.append(np.mean(Allsum))
    FinalPhase1Per.append(np.mean(Allphase1_activity_per))
    
    

