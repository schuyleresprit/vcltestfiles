import geocoder
import pandas as pd
import json

key = "pk.eyJ1Ijoic2NodXlsZXJlIiwiYSI6ImNsMjk4dHhsZTAxNGQzY3VwNnc1b2Z5d2MifQ.dFwDS9kaYpkp_GbJmN2QOg"

addresses_df = pd.read_csv("vclpubplaces.csv")

addresses = addresses_df["pub_location"].values.tolist()
latitudes = []
longitudes = []

for address in addresses:
	result = geocoder.mapbox(address, no_annotations="1")

	if result:
		longitude = (result.lng)
		latitude = (result.lat)
	else:
		longitude = "N/A"
		latitude = "N/A"

	latitudes.append(latitude)
	longitudes.append(longitude)

addresses_df["Latitudes"] = latitudes
addresses_df["Longitudes"] = longitudes

addresses_df.to_csv("vclpubplaces_geocoded.csv")
