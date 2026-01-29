import requests

def get_elevation_gain(coords):
 
    if not coords:
        return 0

    # Build locations payload
    locations = [{"latitude": lat, "longitude": lon} for lat, lon in coords]

    url = "https://api.open-elevation.com/api/v1/lookup"
    response = requests.post(url, json={"locations": locations})

    if response.status_code != 200:
        raise Exception(f"Elevation API error: {response.status_code}")

    data = response.json()
    elevations = [r["elevation"] for r in data["results"]]

    gain = 0
    for i in range(1, len(elevations)):
        diff = elevations[i] - elevations[i - 1]
        if diff > 0:
            gain += diff

    return gain
