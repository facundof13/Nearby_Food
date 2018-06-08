import googlemaps
import time
import re
import zipcodes
import random
import config

# Starting variables
gmaps = googlemaps.Client(key=config.api_key)
choices = ['food', 'mexican', 'italian', 'american', 'pizza', 'fast food', 'indian', 'chinese', 'brunch']
all_locations = []

# Grab and validate user zipcode
valid_zip = re.compile("^\d{5}")
zip_code = 0
zip_code2 = 0
zip_code3 = 0
while True:
    zip_code = input("Enter your zip code: ")
    if  valid_zip.match(zip_code) and len(zip_code) == 5:
        break

print("Enter a category:")
print("0. No Category")
print("1. Mexican")
print("2. Italian")
print("3. American")
print("4. Pizza")
print("5. Fast Food")
print("6. Indian")
print("7. Chinese")
print ("8. Brunch")

while True:
    choice = input("Enter 0 - " + str(len(choices) - 1) + ": ")
    if choice.isnumeric() and int(choice) >= 0 and int(choice) <=len(choices):
        break

print ("Deciding for you...")
print ("This could take up to 15 seconds...")

choice = int(choice)
search_term = choices[choice]


zip_code2 = int(zip_code) + 1
zip_code3 = int(zip_code) - 1

# Convert zipcode to lat and long
location = tuple([zipcodes.matching(zip_code)[0]['lat'], zipcodes.matching(zip_code)[0]['long']])
location2 = tuple([zipcodes.matching(str(zip_code2))[0]['lat'], zipcodes.matching(str(zip_code2))[0]['long']])
location3 = tuple([zipcodes.matching(str(zip_code3))[0]['lat'], zipcodes.matching(str(zip_code3))[0]['long']])

# Find the results nearby
results = (gmaps.places(search_term, location, radius = 3000, type="restaurant"))
time.sleep(2)
results2 = (gmaps.places(search_term, location, page_token=results["next_page_token"]))
time.sleep(2)
results3 = (gmaps.places(search_term, location, page_token=results2["next_page_token"]))

results4 = (gmaps.places(search_term, location2, radius = 3000, type="restaurant"))
time.sleep(2)
results5 = (gmaps.places(search_term, location2, page_token=results4["next_page_token"]))
time.sleep(2)
results6 = (gmaps.places(search_term, location2, page_token=results5["next_page_token"]))

results7 = (gmaps.places(search_term, location3, radius = 3000, type="restaurant"))
time.sleep(2)
results8 = (gmaps.places(search_term, location3, page_token=results7["next_page_token"]))
time.sleep(2)
results9 = (gmaps.places(search_term, location3, page_token=results8["next_page_token"]))

# Append all results to the array
for i in range(0, len(results)):
    if results['results'][i]['name'] not in all_locations:
        all_locations.append(results['results'][i]['name'])
for i in range(0, len(results2)):
    if results2['results'][i]['name'] not in all_locations:
        all_locations.append(results2['results'][i]['name'])
for i in range(0, len(results3)):
    if results3['results'][i]['name'] not in all_locations:
        all_locations.append(results3['results'][i]['name'])

for i in range(0, len(results4)):
    if results4['results'][i]['name'] not in all_locations:
        all_locations.append(results4['results'][i]['name'])
for i in range(0, len(results5)):
    if results5['results'][i]['name'] not in all_locations:
        all_locations.append(results5['results'][i]['name'])
for i in range(0, len(results6)):
    if results6['results'][i]['name'] not in all_locations:
        all_locations.append(results6['results'][i]['name'])

for i in range(0, len(results7)):
    if results7['results'][i]['name'] not in all_locations:
        all_locations.append(results7['results'][i]['name'])
for i in range(0, len(results8)):
    if results8['results'][i]['name'] not in all_locations:
        all_locations.append(results8['results'][i]['name'])
for i in range(0, len(results9)):
    if results9['results'][i]['name'] not in all_locations:
        all_locations.append(results9['results'][i]['name'])

# return a random location
print ("\t" + random.choice(all_locations))

# Print all choices if user decides
answer = input("Would you like to see all choices? Enter y/n: ")
if answer.lower() == 'y' or answer.lower() == 'yes':
    for item in all_locations:
        print ("\t" + item)