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
Include function for plotting scano timeseries (see scanotron_magic_BHS) and downsampling to average of timespans.
Include function for plotting INP various plots
Include function for creating error bars for scanotron and ice nucleating particles (the INP uncertainties are created in spreadsheet, but more needs to be done before they can be plotted..see PEACETIME notebook)
Include function for calculating INP concentrations normalized by particle surface area (see in_bio_analysis notebook)
Include function for calculating correlation terms (see PEACETIME notebooks)
Include function for calculating particle surface areas (see in_bio_analysis notebook)
'''


#__all__=["calculate_raw","calculate_raw_blank","clean_inverted","clean_magic","load_scano_data"]



print('heyedede')
