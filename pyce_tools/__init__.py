import pandas as pd
import os
import math
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import datetime
import random

quotes = ["Let's kick some ice!","Cool party!","What killed the dinosaurs? The Ice Age!",
    "In this universe, there's only one absolute... everything freezes!","Allow me to break the ice: My name is Freeze. Learn it well, for it's the chilling sound of your doom.",
    "Tonight's forecast... a freeze is coming!","The Ice Man cometh!","If revenge is a dish best served cold, then put on your Sunday finest. It's time to feast!",
    "Gotham city needs to chill","Stay frosty","ice to meet you."]

print(quotes[random.randint(0,len(quotes)-1)])
