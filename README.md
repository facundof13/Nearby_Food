# Nearby Food

Ever have difficulty choosing where to go eat? Have too many choices? Worry no more, as this simple python script chooses a place to eat for you.

## How This Works
Nearby Food uses the [Google Places API](https://developers.google.com/places/web-service/search) to find nearby restaurants based on a number of food categories. A random location is then chosen for you. 

## How to set up

1. Head over to [this link](https://console.developers.google.com/apis/dashboard) and create a new project
2. Get a Google maps api key
3. Create a new file titled **config.py** in the project directory
4. Paste this code into the file:
	> api_key =  "[YOUR KEY HERE]"
5. Make sure you've installed all the required pip modules

### Modules to install

 - pip install googlemaps
 - pip install zipcodes