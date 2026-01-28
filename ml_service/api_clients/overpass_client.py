import requests  # import HTTP library

def get_trail_coordinates(trail_name, area=None):

    query = f"""
    [out:json];
    way["name"="{trail_name}"];
    out geom;
    """
    url = "http://overpass-api.de/api/interpreter"
    response = requests.post(url, data=query)
    
    if response.status_code != 200:  # check if API works
        raise Exception(f"Overpass API error: {response.status_code}")
    
    data = response.json()  # parse JSON response
    coordinates = []
    for element in data.get("elements", []):
        if "geometry" in element:
            for point in element["geometry"]:
                coordinates.append((point["lat"], point["lon"]))
    return coordinates
