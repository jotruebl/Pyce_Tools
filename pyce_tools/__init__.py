import pandas as pd
import os
import math
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import datetime

#from . import pyce_tools.calculate_raw_blank, 
#pyce_tools.calculate_raw, pyce_tools.clean_inverted, pyce_tools.clean_magic, pyce_tools.load_scano_data



'''
TODO:
DONE Include function for plotting scano timeseries with error bars (see scanotron_magic_BHS) --> def plot_number_dist
DONE Include function for calculating particle surface areas (see in_bio_analysis notebook) --> def surface_area
DONE Function for plotting scano surface area time series with error bars --> def plot_surface_dist
Function for downsampling to average of timespans.
Handle Time Zones
Include function for plotting INP various plots
Include function for creating error bars for ice nucleating particles (the INP uncertainties are created in spreadsheet, but more needs to be done before they can be plotted..see PEACETIME notebook)
Include function for calculating INP concentrations normalized by particle surface area (see in_bio_analysis notebook)
Include function for calculating correlation terms (see PEACETIME notebooks)
Include function for plotting INP compared with previous studies
'''


#__all__=["calculate_raw","calculate_raw_blank","clean_inverted","clean_magic","load_scano_data"]



print('heyedede')
