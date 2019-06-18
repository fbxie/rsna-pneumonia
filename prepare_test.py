#!/usr/bin/env python3
"""
Script for preparing data for the RSNA Pneumonia Detection Challenge
"""
import json
import glob
import os
from collections import defaultdict
import pandas as pd
from sklearn.model_selection import StratifiedKFold
import util

sz = 1000
with open('settings.json') as json_data_file:
    json_data = json.load(json_data_file)


test_jpg_dir = json_data["TEST_JPG_DIR"]
if not os.path.exists(test_jpg_dir):
    os.mkdir(test_jpg_dir)

    for i, dcm_file in enumerate(glob.glob(os.path.join(json_data["TEST_DCM_DIR"], "*.dcm"))):
        bn = os.path.basename(dcm_file)
        out_file = os.path.join(test_jpg_dir, bn[:-4]+".jpg")
        print(f"Converting test image # {i+1}\r", end="")
        util.dicom_to_jpg(dcm_file, out_file, sz)
print()
