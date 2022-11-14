'''
Get live weather feeds from Guersey Airport
Note that the web page contains frames withon frames
Therefore we need to find the urls of the inner frames
First search for "middle" frame and then the "left" frame
The data we want is then embedded in <font> tags
Note the all these frames are encoded with "windows-1252" and NOT utf-8
'''
import numpy as np

import re
from urllib.request import urlopen


def get_met_data():
    def get_frame_url(url, frame_name):
        with urlopen(url) as response:
            body = response.read().decode("windows-1252")
            try:
                pattern = rf'<frame.*{frame_name}.*src="([^ ]*)"'
                m = re.search(pattern, body)
                if m:
                    frame_url = m.group(1)
            except Exception as e:
                print("*********", e)
        return frame_url

    base = "http://www.metoffice.gov.gg/met/" 
    url = f"{base}LiveDataFrames.htm"
    middleUrl = f"{base}{get_frame_url(url, 'middle')}"
    leftUrl = f"{base}{get_frame_url(middleUrl, 'left')}"
    results = []
    with urlopen(leftUrl) as response:
        try:
            body = response.read().decode("windows-1252")
            pattern = r'<font.*?>([0-9.]+?)</font>'
            for matcher in re.finditer(pattern, body):
                if matcher:
                    data = matcher.group(1)
                    results.append(data)
        except Exception as e:
            print("*********", e)
    return results

print("Met Data from Guernsey Airport")
text = ["Sea Level Pressure (mb)", "pressure change", "Relative Humidity (%)", "Air Temperature (°C)", "Dew Point (°C)", "mb"]
results = get_met_data()
for t, d in zip(results, text):
    print(f"{d:25s} = {t}")






