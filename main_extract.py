#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:31:45 2020

@author: florian
"""


import threading 
import datetime
from extract_data import extract


def update():
    getData()
    set_timer()

  

def set_timer():
    timer = threading.Timer( 60*60 , update) # 10 = duration in second
    timer.start()
    if iteration ==95:
        timer.cancel()

  

def main():
    global iteration
    iteration = 1
    update()

def getData():
    global iteration
    
    a = extract()
    with open ('allData.csv', 'a') as allData:
        a.to_csv( allData, header=True, index=False)
    print(iteration, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    iteration = iteration +1
    
    
    






    
    
    