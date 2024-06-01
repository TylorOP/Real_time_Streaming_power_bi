# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
from datetime import datetime

import requests
import time
import random

##class for data_generation


def data_generation():
    surr_id = random.randint(1, 3)
    speed = random.randint(20,200)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()
    

    return [surr_id, speed, date, time]


if __name__ == '__main__':   

    REST_API_URL = 'https://api.powerbi.com/beta/fbe06994-8712-45a7-9df4-7b63bfbac036/datasets/eaac79a1-29b3-4f3d-b82f-9c16244ae2df/rows?clientSideAuth=0&experience=power-bi&key=aSjCiZiugXQf7oGeRyQAxvUwkUnsbAla52kH5HAz0DUeuhH13iWZW55RRzhFIGOKUjJ09RdAwwC3j6HS1m7fxA%3D%3D'
    
    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["surr_id", "speed", "date", "time"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)

        print("Data posted in Power BI API")
        time.sleep(2)
