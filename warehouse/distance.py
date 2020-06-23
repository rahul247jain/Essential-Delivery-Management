from math import sin, cos, sqrt, atan2, radians
import json


def cor_dist_calculator(lat1, lat2, lon1, lon2):
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance  # Change to return result instead of printing


cities = {
    "Ahmedabad": "23.02579,72.58727",
    "Bengaluru": "12.97194,77.59369",
    "Chennai": "13.08784,80.27847",
    "Chittorgarh": "24.879999,74.629997",
    "Jodhpur": "26.263863, 73.008957",
    "Raipur": "21.250000 ,81.629997",
    "Sirohi": "24.882618,72.858894",
    "Pali":	"25.771315,73.323685",
    "Delhi": "28.65195,77.23149",
    "Hyderabad": "17.38405,78.45636",
    "Kanpur": "26.46523,80.34975",
    "Kolkata": "22.56263,88.36304",
    "Mumbai": "19.07283,72.88261",
    "Ratnagiri": "16.994444 , 73.300003",
    "Pune": "18.51957,73.85535",
    "Surat": "21.19594,72.83023",
    "Sultanpur": "26.264776, 82.072708",
    "Lucknow": "26.839281,80.923133",
    "Patna": "25.615379,85.101027",
    "Indore": "22.717736,75.85859",
    "Vadodara": "22.299405,73.208119",
    "Bhopal": "23.254688,77.402892",
    "Coimbatore": "11.005547,76.966122",
    "Agra": "27.187935,78.003944",
    "Meerut": "28.980018,77.706356",
    "Madurai": "9.917347,78.119622",
    "Guwahati": "26.176076,91.762932",
    "Thiruvananthapuram": "8.485498,76.949238",
    "Tiruchchirappalli": "10.815499,78.696513",
    "Kota": "25.182544,75.839065",
    "Jammu": "32.735686,74.869112",
    "Mangalore": "12.865371,74.842432",
    "Ajmer": "26.452103,74.638667",
    "Shillong": "25.573987,91.896807",
    "New Delhi": "28.6,77.2"
}

# result = { } # result cache
# c1=request.POST.get('city')
# lat1 , lon1 = cities.get(c1).split(",")
c1 = "Jodhpur"
lat1 = 26.263863
lon1 = 73.008957

min = 10000000000.00
for c2, o2 in cities.items():
    if c1 == c2:  # Skip distance to itself
        min = 0
        break
    lat2, lon2 = o2.split(",")
    lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)
    dist = cor_dist_calculator(radians(lat1), radians(
        lat2), radians(lon1), radians(lon2))
    print(dist, "Kms")
    if dist < min:
        min = dist


# Use JSON to pretty print
print("Min dist = ", min)
