import pandas as pd
import os
import math
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import datetime
import random



#from . import pyce_tools.calculate_raw_blank, 
#pyce_tools.calculate_raw, pyce_tools.clean_inverted, pyce_tools.clean_magic, pyce_tools.load_scano_data



'''
TODO:
Function for downsampling to average of timespans.
Handle Time Zones
Include function for plotting INP various plots
DONE? Include function for creating error bars for ice nucleating particles (the INP uncertainties are created in spreadsheet, but more needs to be done before they can be plotted..see PEACETIME notebook)
DONE? Include function for calculating INP concentrations normalized by particle surface area (see in_bio_analysis notebook)
DONE? Include function for calculating correlation terms (see PEACETIME notebooks)
DONE? Include function for plotting INP compared with previous studies
'''


#__all__=["calculate_raw","calculate_raw_blank","clean_inverted","clean_magic","load_scano_data"]

quotes = ["Let's kick some ice!","Cool party!","What killed the dinosaurs? The Ice Age!",
    "In this universe, there's only one absolute... everything freezes!","Allow me to break the ice: My name is Freeze. Learn it well, for it's the chilling sound of your doom.",
    "Tonight's forecast... a freeze is coming!","The Ice Man cometh!","If revenge is a dish best served cold, then put on your Sunday finest. It's time to feast!",
    "Gotham city needs to chill","Stay frosty","ice to meet you."]

print(quotes[random.randint(0,len(quotes)-1)])
