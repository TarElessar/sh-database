# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:31:14 2022

@author: felix
"""


import os
import pandas as pd

EXCEL_FILES = [r"D:\git\sh-database\data_raw\Sandra Character Spreadsheet.xlsx"]

OUTPUT_FILE = r"D:\git\sh-database\setup\data_raw\spreadsheet_master.csv"

for file in EXCEL_FILES:
    df_partial = pd.read_excel(file)
    
    print(df_partial)