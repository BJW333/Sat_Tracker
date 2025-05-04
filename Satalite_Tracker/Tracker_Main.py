import os
from pathlib import Path
import requests
from skyfield.api import load, EarthSatellite
import folium
import time 

script_dir = Path(__file__).parent
print("Script Directory:", script_dir)

def fetch_tle_data():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    response = requests.get(url)
    print("Fetching TLE data from:", url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch TLE data: {response.status_code}")
    print("TLE data fetched successfully")
    return response.text.strip().split("\n")


def get_data_of_SAT(tle_lines):
    satellites = []
    for i in range(0, len(tle_lines)-2, 3):
        name, line1, line2 = tle_lines[i], tle_lines[i+1], tle_lines[i+2]
        sat = EarthSatellite(line1, line2, name)
        satellites.append(sat)
    print(f"Loaded {len(satellites)} satellites.")
    return satellites

def create_map():
    tle_lines = fetch_tle_data()
    sats_in_space = get_data_of_SAT(tle_lines)
    
    sat_map = folium.Map(location=[0, 0], zoom_start=2)
    
    ts = load.timescale()
    t = ts.now()
    
    for sat in sats_in_space:
        geocentric = sat.at(t)
        subpoint = geocentric.subpoint()
        lat, lon, altitude = subpoint.latitude.degrees, subpoint.longitude.degrees, subpoint.elevation.km

        folium.CircleMarker(
           location=[lat, lon],
           radius=1.5,
           color='blue',
           fill=True,
           fill_opacity=0.7,
           popup=f'{sat.name}<br>Altitude: {altitude:.2f} km'
        ).add_to(sat_map)
        
    sat_map.save(script_dir / "sat_map.html")
    
  
def tracker_main():
    create_map()
    print("Map updated.")
    time.sleep(60)
        
if __name__ == "__main__":
    tracker_main()
    print("Tracker started.")