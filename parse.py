#Open csv files to get the information of the request

import csv
import csvConst
import os 
CSV_FOLDER = os.path.dirname(os.path.realpath(__file__)) + "\\gtfs_stm-181203-190324\\"
FILE_ROUTES = CSV_FOLDER + "routes.txt"
FILE_TRIP = CSV_FOLDER + "trips.txt"
FILE_STOP_TIMES= CSV_FOLDER + "stop_times.txt"
FILE_STOPS = CSV_FOLDER + "stops.txt"

csv.register_dialect('defaultDialect',
delimiter = ',',
skipinitialspace=True)
#csv.field_size_limit([new_limit])
#       Returns the current maximum field size allowed by the parser. If new_limit is given, this becomes the new limit.



def find(file, key, returnColumn ):
    with open(file, 'r') as csvFile:
        csvReader = csv.reader(csvFile, dialect='defaultDialect')

        for row in csvReader:

            if row[key.column] == key.value:
                return row[returnColumn]



def findAll(file, key, returnColumn ):
    returnList = []
    
    values =[]

    for singleKey in key:
        values.append(singleKey.value)


    with open(file, 'r') as csvFile:
        csvReader = csv.reader(csvFile, dialect='defaultDialect')

        for row in csvReader:

            if row[key[0].column] in values:
                returnList.append(row[returnColumn])


    return returnList



#Key for resarch in csv file
class Key:

    def __init__(self, value, column):
        self.value = value
        self.column = column

#find the route id of route from its short name (line)
def findRouteID(lineNb):
    key = Key(value = lineNb, column = csvConst.ROUTES__SHORT_NAME)
    return find(FILE_ROUTES, key, csvConst.ROUTES__ROUTE_ID)


#find the trip id of trip from the route id
def findTripID(routeId):
    key = Key(value = routeId, column = csvConst.TRIPS__ROUTE_ID)
    return find(FILE_TRIP, key, csvConst.TRIPS__TRIP_ID)

def findAllStopIds(tripId):
    
    key = Key(value = tripId, column = csvConst.STOP_TIMES__TRIP_ID)
    return findAll(FILE_STOP_TIMES, [key], csvConst.STOP_TIMES__STOP_ID)


def findStopsNames(stopId):

    key = []
    for singleStopId in stopId:
        key.append(Key(value = singleStopId, column =csvConst.STOPS__STOP_ID))
    return findAll(FILE_STOPS, key, csvConst.STOPS__STOP_NAME)

def findStops(lineNb):
    routeId = findRouteID(lineNb)

    tripId = findTripID(routeId)

    stopIds = findAllStopIds(tripId)

    return findStopsNames(stopIds)
    

def findLine( search):

    findLineWithNumber(search)


def main():
    print(findStops("10"))

if (__name__ == "__main__"):
    main()
