Satellite Tracker

This Python program fetches live satellite data from CelesTrak, computes their subpoints using the Skyfield library, and plots their current positions on an interactive world map using Folium.

The output is saved as a sat_map.html file, which can be opened in any web browser to visualize real-time satellite locations.

⸻

Features
	•	Fetches real-time TLE (Two-Line Element) data for active satellites from CelesTrak
	•	Uses Skyfield to calculate the subpoint (position directly below the satellite on Earth)
	•	Generates a world map with satellite markers using Folium
	•	Updates every run (optionally extend it for automatic refreshing in intervals)

⸻

After running the program open sat_map.html in your browser to explore.

⸻

License

MIT License
