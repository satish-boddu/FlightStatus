import time
import datetime
import requests
import json
import os

# Flight Status

	# Flight Status by ID and API URL 
		# Example
		# flight_stat_url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/QR/1/arr/2018/08/21?appId=***&appKey=***&utc=false"
	# Flight Status by Route and API URL
		# Example
		# flight_stat_url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/route/status/DOH/LHR/dep/2018/08/21?appId=***&appKey=***&hourOfDay=0&utc=false&numHours=24"
	# Flight Status by ID and Web Scrapping 
		# Example
		# flight_stat_url = "https://www.flightstats.com/v2/flight-tracker/AA/18?year=2018&month=8&date=21"

def api_url_generator(host, appID, apiKey):
	print("How would you like to search for your flight?")
	method = input("By Route or Flight_ID? {route, id}: ")
	url = host
	os.system('clear')

	if method in ["route", "r", "R", "Route", "ROUTE"]:
		url += "route/status/"

		# Adding the Departure and Arrival Airports
		print("Please Enter the 3 Character Code for the Airports (Ex. LHR - London Heathrow, DOH - Doha Hamad Int'l)")
		from_air = input("From: ")
		# ** ** Need to make a validate function
		# validate_airport_code(from_air)
		to_air = input("To: ")
		# ** ** Need to make a validate function
		# validate_airport_code(from_air)
		url += from_air +  '/' + to_air + '/dep/'
		
		os.system('clear')

		# Adding the Departure Date on which we search for flights
		print ("From: ", from_air, " --> ", "To: ", to_air)
		print ()
		print ('Please enter you departure date')
		dep_year = input('Year (YYYY): ')
		dep_month = input('Month (MM): ')
		dep_day = input('Day (DD): ')
		if (dep_year == '') or (dep_month == '') or (dep_day == ''):
			dep_year = str(datetime.datetime.now().year)
			dep_month = str(datetime.datetime.now().month)
			dep_day = str(datetime.datetime.now().day)
		url += dep_year + '/' + dep_month + '/' + dep_day

		# Adding the Api Key and the remaining fields
		url += '?appId=' + appID + '&appKey=' + apiKey + '&hourOfDay=' + '0' + '&numHours=' + '24' + '&utc=false'
		return url

	elif method in ["id", "Id", "ID", "Flight_ID", "flight_id", "Flight ID", "flight id", "flight_ID", "flight ID"]:
		url += "flight/status/"

		# Adding the flight code
		air_code = input('Please Enter the Airline Code (Ex. QR -> Qatar Airways, BA -> British Airways): ')
		# ** ** Need to make a validate function
		flight_no = input('Please Enter the Flight no.: ')
		url += air_code + '/' + flight_no + '/dep/'
		print ()
		print ('Please enter you departure date')
		dep_year = input('Year (YYYY): ')
		dep_month = input('Month (MM): ')
		dep_day = input('Day (DD): ')
		if (dep_year == '') or (dep_month == '') or (dep_day == ''):
			dep_year = str(datetime.datetime.now().year)
			dep_month = str(datetime.datetime.now().month)
			dep_day = str(datetime.datetime.now().day)
		url += dep_year + '/' + dep_month + '/' + dep_day

		# Adding the Api Key and the remaining fields
		url += '?appId=' + appID + '&appKey=' + apiKey + '&utc=false'
		return url

	else:
		try_again = input("Sorry Wrong Input! Do you want to retry? (y/n): ")
		if try_again in ['y', 'Y', 'Yes', 'yes', 'YES']:
			os.system('clear')
			api_url_generator(host, appID, apiKey)
		else:
			return 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/UFO/109090/arr/5000/50/50?appId=c0108d04&appKey=a05ff275a408df68c013da1bc00d4046&utc=false'



def airlines(data, code):
	if data['appendix']['airlines']:
		for airline in data['appendix']['airlines']:
			if airline['fs'] == code:
				return airline['name']
		return "Error: Airlines Not Found"
	else:
		return "Error: No Airlines Available"



def airport(data, code):
	if data['appendix']['airports']:
		for airport in data['appendix']['airports']:
			if airport['fs'] == code:
				return airport['name'] + " - " + airport['city']
		return "Error: No such Airport Not Found"
	else:
		return "Error: No Airports Available"



def strtots(string):
	y = int(string[:4])
	m = int(string[5:7])
	d = int(string[8:10])
	h = int(string[11:13])
	mi = int(string[14:16])
	dt = datetime.datetime(y, m, d, h, mi)
	return time.mktime(dt.timetuple())



def timediff(arr, dep):
	departure = strtots(dep)
	arrival = strtots(arr)

	duration = arrival - departure
	return time.strftime("%H:%M", time.gmtime(duration))



def departed(data):
	print()
	# 	* Actual Departure Time
	try:
		ADT = data['operationalTimes']['actualGateDeparture']['dateLocal']
	except KeyError:
		ADT = data['operationalTimes']['scheduledGateDeparture']['dateLocal']                                                                                                                                                                                                                                                                                                                                                                                                             
	ADTime = ADT.split('T')
	ADTime = ADTime[1].split(':')
	ADTime = ADTime[0] + ':' + ADTime[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
	print('\tActual Departure Time: ', '\t', ADTime)

	# 	* Time left on journey
	current_time = str(datetime.datetime.utcnow().isoformat())
	try:
		UtcSAT = data['operationalTimes']['estimatedGateArrival']['dateUtc']
	except KeyError:
		UtcSAT = data['operationalTimes']['scheduledGateArrival']['dateUtc']

	rem_time = timediff(UtcSAT, current_time)
	rem_time = rem_time.split(':')
	rem_time = rem_time[0] + 'hrs ' + rem_time[1] + 'min'
	print('\tArriving at Destination in: ', '\t', rem_time)

	# 	* Scheduled Arrival Time
	SAT = data['operationalTimes']['scheduledGateArrival']['dateLocal']
	SATime = SAT.split('T')
	SATime = SATime[1].split(':')
	SATime = SATime[0] + ':' + SATime[1]
	print('\tScheduled Arrival Time: ', '\t', SATime)



def arrived(data):
	print()
	# 	* Actual Departure Time
	try:
		ADT = data['operationalTimes']['actualGateDeparture']['dateLocal']
	except KeyError:
		ADT = data['operationalTimes']['scheduledGateDeparture']['dateLocal']                                                                                                                                                                                                                                                                                                                                                                                                             
	ADTime = ADT.split('T')
	ADTime = ADTime[1].split(':')
	ADTime = ADTime[0] + ':' + ADTime[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
	print('\tActual Departure Time: ', '\t', ADTime)

	# 	* Actual Arrival Time
	try:
		AAT = data['operationalTimes']['actualGateArrival']['dateLocal']
	except KeyError:
		AAT = data['operationalTimes']['scheduledGateArrival']['dateLocal']
	AATime = AAT.split('T')
	AATime = AATime[1].split(':')
	AATime = AATime[0] + ':' + AATime[1]
	print('\tActual Arrival Time: ', '\t', AATime)

	# 	* Journey Time
	try:
		AAT = data['operationalTimes']['actualGateArrival']['dateUtc']
	except KeyError:
		AAT = data['operationalTimes']['scheduledGateArrival']['dateUtc']
	try:
		ADT = data['operationalTimes']['actualGateDeparture']['dateUtc']
	except KeyError:
		ADT = data['operationalTimes']['scheduledGateDeparture']['dateUtc']
	jour_time = timediff(AAT, ADT)        
	jour_time = jour_time.split(':')
	jour_time = jour_time[0] + 'hrs ' + jour_time[1] + 'min'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
	print('\tDuration of Journey: ', '\t', jour_time)

	#	* Time Since Flight Landed
	current_time = str(datetime.datetime.utcnow().isoformat())
	past_time = timediff(current_time, AAT)
	past_time = past_time.split(':')
	past_time = past_time[0] + 'hrs ' + past_time[1] + 'min'
	print('\tTime Since Flight Landed: ', '\t', past_time)



def scheduled(data):
	print()
	# 	* Scheduled Departure Time
	SDT = data['operationalTimes']['scheduledGateDeparture']['dateLocal']
	SDTime = SDT.split('T')
	SDTime = SDTime[1].split(':')
	SDTime = SDTime[0] + ':' + SDTime[1]
	print('\tScheduled Departure Time: ', '\t', SDTime)

	# 	* Scheduled Arrival Time
	SAT = data['operationalTimes']['scheduledGateArrival']['dateLocal']
	SATime = SAT.split('T')
	SATime = SATime[1].split(':')
	SATime = SATime[0] + ':' + SATime[1]
	print('\tScheduled Arrival Time: ', '\t', SATime)

	# 	* Estimated Journey Begin Time
	current_time = str(datetime.datetime.utcnow().isoformat())
	rem_time = timediff(data['operationalTimes']['scheduledGateDeparture']['dateUtc'], current_time)
	rem_time = rem_time.split(':')
	rem_time = rem_time[0] + 'hrs ' + rem_time[1] + 'min'
	print('\tFlight Departs in: ', '\t', rem_time)



def output(data):
	statuses = {"A":"Departed", "C":"Canceled", 'D':'Diverted',\
				'DN':'Data source needed', 'L':'Landed', \
				'NO':'Not Operational', 'R':'Redirected', \
				'S':'Scheduled', 'U':'Unknown'}

	if data['flightStatuses']:
		print ("Found ", len(data['flightStatuses'])," flight/s for the information provided.")
		print ("The Flights Data is presented below: ")
		print("******************************************************************************")
		for flight in data['flightStatuses']:
			print("\tFlight No.: ", '\t', flight["carrierFsCode"], flight["flightNumber"])
			print("\tAirlines: ", '\t', airlines(data, flight["carrierFsCode"]))
			print()
			print("\tFrom: ", '\t', flight["departureAirportFsCode"], '\t', airport(data, flight["departureAirportFsCode"]))
			print("\tTo: ", '\t', flight["arrivalAirportFsCode"], '\t', airport(data, flight["arrivalAirportFsCode"]))
			print()
			print("\tStatus: ", statuses[flight["status"]])
			if statuses[flight["status"]] == 'Departed':
				#Run the Departed Code
				departed(flight)
			elif statuses[flight["status"]] == 'Landed':
				#Run the Arrived Code
				arrived(flight)
			elif statuses[flight["status"]] == 'Scheduled':
				#Run the Scheduled Code
				scheduled(flight)
			print("******************************************************************************")

	else:
		print ("Sorry! No Flights found matching your description. Please check all fields and try again :)")



def airport_data_salvager(data):
	airports_path = 'Data/airports.json'
	airports = data['appendix']['airports']
	counter = 0
	new_airports = []
	for airport in airports:
		del_fields = ['iata', 'icao', 'localTime', 'classification', 'active', 'delayIndexUrl', 'weatherUrl']
		for field in del_fields:
			try:
				airport.pop(field)
			except KeyError:
				pass
		airport_name = airport['fs'] + ' - ' + airport['name'] + ' - ' + airport['city']
		airport['airport'] = airport_name

		if os.path.exists(airports_path):
			airports_data = json.load(open(airports_path, 'r'))
			if airport not in airports_data:
				airports_data.append(airport)
				counter += 1
				new_airports.append(airport['fs'] + ' - ' + airport['city'])
			with open(airports_path, "w") as ports_json:
				json.dump(airports_data, ports_json)
			
			
		else:
			airports_data = []
			if airport not in airports_data:
				airports_data.append(airport)
				counter += 1
				new_airports.append(airport['fs'] + ' - ' + airport['city'])
			with open(airports_path, "w") as ports_json:
				json.dump(airports_data, ports_json)
			

	if counter > 1:
		print (counter, " New airports have been saved to the local storage. They are: ")
		print ()
	elif counter == 1:
		print (counter, " New airport has been saved to the local storage. It is: ")
		print ()
	else:
		print ("No New Airports have been located.")

	if new_airports:
		for i in new_airports:
			print(i)



def airlines_data_salvager(data):
	airlines_path = 'Data/airlines.json'
	airlines = data['appendix']['airlines']
	counter = 0
	new_airports = []
	for airport in airports:
		del_fields = ['iata', 'icao', 'localTime', 'classification', 'active', 'delayIndexUrl', 'weatherUrl']
		for field in del_fields:
			try:
				airport.pop(field)
			except KeyError:
				pass
		airport_name = airport['fs'] + ' - ' + airport['name'] + ' - ' + airport['city']
		airport['airport'] = airport_name

		if os.path.exists(airports_path):
			airports_data = json.load(open(airports_path, 'r'))
			if airport not in airports_data:
				airports_data.append(airport)
				counter += 1
				new_airports.append(airport['fs'] + ' - ' + airport['city'])
			with open(airports_path, "w") as ports_json:
				json.dump(airports_data, ports_json)
			
			
		else:
			airports_data = []
			if airport not in airports_data:
				airports_data.append(airport)
				counter += 1
				new_airports.append(airport['fs'] + ' - ' + airport['city'])
			with open(airports_path, "w") as ports_json:
				json.dump(airports_data, ports_json)
			

	if counter > 1:
		print (counter, " New airports have been saved to the local storage. They are: ")
		print ()
	elif counter == 1:
		print (counter, " New airport has been saved to the local storage. It is: ")
		print ()
	else:
		print ("No New Airports have been located.")

	if new_airports:
		for i in new_airports:
			print(i)
	# # TO READ FROM AIRPORTS FILE
 #    data = json.load(open(path, 'r'))

	# # TO WRITE TO AIRPORTS FILE
	# with open(airports_path, "w") as ports_json:
 #                    json.dump(data, ports_json)








os.system('clear')
# Creating the API URL 
host = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/"
appID = "***"
apiKey = "***"

flight_stat_url = api_url_generator(host, appID, apiKey)
os.system('clear')





data = requests.get(flight_stat_url).text
data = json.loads(data)

output(data)
#data_salvager(data)


print ("Demographics")	
airports_data = json.load(open('Data/airports.json', 'r'))
countries = []
count = 0
for i in airports_data:
	if i['countryName'] not in countries:
		countries.append(i['countryName'])
	if i['regionName'] == 'Africa':
		count += 1
print("Total No. of airports collected: ", len(airports_data))
print("Total No. of unique countries in airports collected: ", len(countries))
print("Total Airports collected in Africa: ", count)



























# Airport Status
airport_url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/airport/status/ABQ/arr/2018/08/17/22?appId=***&appKey=***&utc=false&numHours=1"
	#Airport Status Web Scrapping
	#"https://www.flightstats.com/v2/airport-conditions/YKF"










'''
data = {
		 "request": {
			  "airline": {
			   "requestedCode": "AA",
			   "fsCode": "AA"
			  },
			  "flight": {
			   "requested": "100",
			   "interpreted": "100"
			  },
			  "date": {
			   "year": "2018",
			   "month": "8",
			   "day": "20",
			   "interpreted": "2018-08-20"
			  },
			  "utc": {
			   "requested": "false",
			   "interpreted": false
			  },
			  "airport": {},
			  "codeType": {},
			  "extendedOptions": {},
			  "url": "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/AA/100/arr/2018/08/20"
		 },
		 "appendix": {
			  "airlines": [
				   {
				    "fs": "AA",
				    "iata": "AA",
				    "icao": "AAL",
				    "name": "American Airlines",
				    "phoneNumber": "08457-567-567",
				    "active": true
				   },
				   {
				    "fs": "LY",
				    "iata": "LY",
				    "icao": "ELY",
				    "name": "El Al",
				    "phoneNumber": "+ 972-3-9771111",
				    "active": true
				   },
				   {
				    "fs": "AY",
				    "iata": "AY",
				    "icao": "FIN",
				    "name": "Finnair",
				    "phoneNumber": "+ 358 600 140 140",
				    "active": true
				   },
				   {
				    "fs": "IB",
				    "iata": "IB",
				    "icao": "IBE",
				    "name": "Iberia",
				    "phoneNumber": "1800 772 4642",
				    "active": true
				   },
				   {
				    "fs": "BA",
				    "iata": "BA",
				    "icao": "BAW",
				    "name": "British Airways",
				    "phoneNumber": "1-800-AIRWAYS",
				    "active": true
				   },
				   {
				    "fs": "GF",
				    "iata": "GF",
				    "icao": "GFA",
				    "name": "Gulf Air",
				    "phoneNumber": "973 17 335 777",
				    "active": true
				   }
			  ],
			  "airports": [
				   {
				    "fs": "JFK",
				    "iata": "JFK",
				    "icao": "KJFK",
				    "faa": "JFK",
				    "name": "John F. Kennedy International Airport",
				    "street1": "JFK Airport",
				    "city": "New York",
				    "cityCode": "NYC",
				    "stateCode": "NY",
				    "postalCode": "11430",
				    "countryCode": "US",
				    "countryName": "United States",
				    "regionName": "North America",
				    "timeZoneRegionName": "America/New_York",
				    "weatherZone": "NYZ178",
				    "localTime": "2018-08-20T22:39:32.176",
				    "utcOffsetHours": -4,
				    "latitude": 40.642335,
				    "longitude": -73.78817,
				    "elevationFeet": 13,
				    "classification": 1,
				    "active": true,
				    "delayIndexUrl": "https://api.flightstats.com/flex/delayindex/rest/v1/json/airports/JFK?codeType=fs",
				    "weatherUrl": "https://api.flightstats.com/flex/weather/rest/v1/json/all/JFK?codeType=fs"
				   },
				   {
				    "fs": "LHR",
				    "iata": "LHR",
				    "icao": "EGLL",
				    "name": "London Heathrow Airport",
				    "city": "London",
				    "cityCode": "LON",
				    "stateCode": "EN",
				    "countryCode": "GB",
				    "countryName": "United Kingdom",
				    "regionName": "Europe",
				    "timeZoneRegionName": "Europe/London",
				    "localTime": "2018-08-21T03:39:32.176",
				    "utcOffsetHours": 1,
				    "latitude": 51.469603,
				    "longitude": -0.453566,
				    "elevationFeet": 80,
				    "classification": 1,
				    "active": true,
				    "delayIndexUrl": "https://api.flightstats.com/flex/delayindex/rest/v1/json/airports/LHR?codeType=fs",
				    "weatherUrl": "https://api.flightstats.com/flex/weather/rest/v1/json/all/LHR?codeType=fs"
				   }
			  ],
			  "equipments": [
				   {
				    "iata": "77W",
				    "name": "Boeing 777-300ER",
				    "turboProp": false,
				    "jet": true,
				    "widebody": true,
				    "regional": false
				   }
		  		]
		 },
		 "flightStatuses": [
			  {
			   "flightId": 970236480,
			   "carrierFsCode": "AA",
			   "flightNumber": "100",
			   "departureAirportFsCode": "JFK",
			   "arrivalAirportFsCode": "LHR",
			   "departureDate": {
				    "dateLocal": "2018-08-19T18:15:00.000",
				    "dateUtc": "2018-08-19T22:15:00.000Z"
				   },
			   "arrivalDate": {
				    "dateLocal": "2018-08-20T06:20:00.000",
				    "dateUtc": "2018-08-20T05:20:00.000Z"
				   },
			   "status": "L",
			   "schedule": {
				    "flightType": "J",
				    "serviceClasses": "RFJY",
				    "restrictions": ""
				   },
			   "operationalTimes": {
				    "publishedDeparture": {
					     "dateLocal": "2018-08-19T18:15:00.000",
					     "dateUtc": "2018-08-19T22:15:00.000Z"
					    },
				    "publishedArrival": {
					     "dateLocal": "2018-08-20T06:20:00.000",
					     "dateUtc": "2018-08-20T05:20:00.000Z"
					    },
				    "scheduledGateDeparture": {
					     "dateLocal": "2018-08-19T18:15:00.000",
					     "dateUtc": "2018-08-19T22:15:00.000Z"
					    },
				    "estimatedGateDeparture": {
					     "dateLocal": "2018-08-19T18:13:00.000",
					     "dateUtc": "2018-08-19T22:13:00.000Z"
					    },
				    "actualGateDeparture": {
					     "dateLocal": "2018-08-19T18:13:00.000",
					     "dateUtc": "2018-08-19T22:13:00.000Z"
					    },
				    "flightPlanPlannedDeparture": {
					     "dateLocal": "2018-08-19T18:56:00.000",
					     "dateUtc": "2018-08-19T22:56:00.000Z"
					    },
				    "estimatedRunwayDeparture": {
					     "dateLocal": "2018-08-19T18:48:00.000",
					     "dateUtc": "2018-08-19T22:48:00.000Z"
					    },
				    "actualRunwayDeparture": {
					     "dateLocal": "2018-08-19T18:48:00.000",
					     "dateUtc": "2018-08-19T22:48:00.000Z"
					    },
				    "scheduledGateArrival": {
					     "dateLocal": "2018-08-20T06:20:00.000",
					     "dateUtc": "2018-08-20T05:20:00.000Z"
					    },
				    "estimatedGateArrival": {
					     "dateLocal": "2018-08-20T06:11:00.000",
					     "dateUtc": "2018-08-20T05:11:00.000Z"
					    },
				    "actualGateArrival": {
					     "dateLocal": "2018-08-20T06:11:00.000",
					     "dateUtc": "2018-08-20T05:11:00.000Z"
					    },
				    "flightPlanPlannedArrival": {
					     "dateLocal": "2018-08-20T06:11:00.000",
					     "dateUtc": "2018-08-20T05:11:00.000Z"
					    },
				    "estimatedRunwayArrival": {
					     "dateLocal": "2018-08-20T06:05:00.000",
					     "dateUtc": "2018-08-20T05:05:00.000Z"
					    },
				    "actualRunwayArrival": {
					     "dateLocal": "2018-08-20T06:05:00.000",
					     "dateUtc": "2018-08-20T05:05:00.000Z"
					    }
				   },
			   "codeshares": [
				    {
				     "fsCode": "AY",
				     "flightNumber": "4012",
				     "relationship": "L"
				    },
				    {
				     "fsCode": "BA",
				     "flightNumber": "1511",
				     "relationship": "L"
				    },
				    {
				     "fsCode": "GF",
				     "flightNumber": "6654",
				     "relationship": "L"
				    },
				    {
				     "fsCode": "IB",
				     "flightNumber": "4218",
				     "relationship": "L"
				    },
				    {
				     "fsCode": "LY",
				     "flightNumber": "8051",
				     "relationship": "L"
				    }
		   		],
			   "flightDurations": {
				    "scheduledBlockMinutes": 425,
				    "blockMinutes": 418,
				    "scheduledAirMinutes": 375,
				    "airMinutes": 377,
				    "scheduledTaxiOutMinutes": 41,
				    "taxiOutMinutes": 35,
				    "scheduledTaxiInMinutes": 9,
				    "taxiInMinutes": 6
			   },
			   "airportResources": {
				    "departureTerminal": "8",
				    "departureGate": "8",
				    "arrivalTerminal": "3",
				    "arrivalGate": "27",
				    "baggage": "10"
			   },
			   "flightEquipment": {
				    "scheduledEquipmentIataCode": "77W",
				    "tailNumber": "N720AN"
				   }
			  }
		 ]
	  }
'''
