import requests, datetime, time, json

#---------- shopping mall carpark data from lta api ------------#
## require api key from LTA ##
## require specific header as as api parameters ##

url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=83139&ServiceNo=15"
headers = {"AccountKey": "5L8Q1wEHRnGxdZwG89iPvQ==",
           "accept": "application/json"}
#headers = {"AccountKey": st.secrets["LTA_APIKEY"],
#           "accept": "application/json"}
response = requests.request(method="get", url=url, headers=headers)
lta_data = response.json()
print(json.dumps(lta_data, indent=4))