import time
import requests
import json


# Flight Status

	# Flight Status by ID and API URL 
		# Example
		# flight_stat_url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/QR/1/arr/2018/08/21?appId=c0108d04&appKey=a05ff275a408df68c013da1bc00d4046&utc=false"
	# Flight Status by ID and Web Scrapping 
		# Example
		# flight_stat_url = "https://www.flightstats.com/v2/flight-tracker/AA/18?year=2018&month=8&date=21"

# Creating the API URL 
host = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/"
appID = "c0108d04127"
apiKey = "a05ff275a408df68c013da1bc00d4046127"

flight_stat_url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/route/status/DOH/LHR/dep/2018/08/21?appId=c0108d04127&appKey=a05ff275a408df68c013da1bc00d4046127&hourOfDay=0&utc=false&numHours=24"

data = requests.get(flight_stat_url).text
data = json.loads(data)

statuses = {"A":"Departed", "C":"Canceled", 'D':'Diverted',\
			'DN':'Data source needed', 'L':'Landed', \
			'NO':'Not Operational', 'R':'Redirected', \
			'S':'Scheduled', 'U':'Unknown'}

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


if data['flightStatuses']:
	print ("Found ", len(data['flightStatuses'])," no. of flights for the information provided.")
	print ("The Flights Data is presented below: ")
	print("*************************************************************")
	for flight in data['flightStatuses']:
		print("\tFlight No.: ", '\t', flight["carrierFsCode"], flight["flightNumber"])
		print("\tAirlines: ", '\t', airlines(data, flight["carrierFsCode"]))
		print()
		print("\tFrom: ", '\t', flight["departureAirportFsCode"], '\t', airport(data, flight["departureAirportFsCode"]))
		print("\tTo: ", '\t', flight["arrivalAirportFsCode"], '\t', airport(data, flight["arrivalAirportFsCode"]))
		print()
		print("\tStatus: ", statuses[flight["status"]])
		print("*************************************************************")




else:
	print ("Sorry! No Flights found matching your description. Please check and try again :)")


	

# Route Status
route_url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/route/status/HYD/DXB/dep/2018/08/15?appId=c0108d04&appKey=a05ff275a408df68c013da1bc00d4046&hourOfDay=0&utc=false&numHours=24"































# Airport Status
airport_url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/airport/status/ABQ/arr/2018/08/17/22?appId=c0108d04&appKey=a05ff275a408df68c013da1bc00d4046&utc=false&numHours=1"
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
