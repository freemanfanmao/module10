import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = "c2a8e2ce179c49bfa49f4b7ec8716744"
INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
  # create an empty list called 'incidents'
    incidents = []
  # use 'requests' to do a GET request to the WMATA Incidents API
    response = requests.get(INCIDENTS_URL, headers = headers)

  # retrieve the JSON from the response
    response_json = response.json()

  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
    if unit_type == 'elevators':
        new_list = [x for x in response_json['ElevatorIncidents'] if x['UnitType'] == 'ELEVATOR']

    if unit_type == 'escalators':
        new_list = [x for x in response_json['ElevatorIncidents'] if x['UnitType'] == 'ESCALATOR']

  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
  #   -StationCode, StationName, UnitType, UnitName
    for i in range(len(new_list)):
        dict = {"StationCode": new_list[i]['StationCode'],
                "StationName": new_list[i]['StationName'],
                "UnitType": new_list[i]['UnitType'],
                "UnitName": new_list[i]['UnitName']}

  # add each incident dictionary object to the 'incidents' list
        incidents.append(dict)

  # return the list of incident dictionaries using json.dumps()
    return json.dumps(incidents)

if __name__ == '__main__':
    app.run(debug=True)
