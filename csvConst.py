###---Constants specific to the csv files format---###

#-routes's columns-#
ROUTES__ROUTE_ID    = 0
ROUTES__AGENCY_ID   = 1
ROUTES__SHORT_NAME  = 2
ROUTES__LONG_NAME   = 3
ROUTES__TYPE        = 4
ROUTES__URL         = 5
ROUTES__COLOR       = 6
ROUTES__TEXT_COLOR  = 7

#-trips's columns-#
TRIPS__ROUTE_ID                 = 0
TRIPS__SERVICE_ID               = 1
TRIPS__TRIP_ID                  = 2
TRIPS__TRIP_HEADSIGN            = 3
TRIPS__DIRECTION_ID             = 4
TRIPS__SHAPE_ID                 = 5
TRIPS__WHEELCHAIR_ACCESSIBLE    = 6
TRIPS__NOTE_FR                  = 7
TRIPS__NOTE_EN                  = 8

#-stop_times's columns-#
STOP_TIMES__TRIP_ID         = 0 
STOP_TIMES__ARRIVAL_TIME    = 1
STOP_TIMES__DEPARTURE_TIME  = 2
STOP_TIMES__STOP_ID         = 3
STOP_TIMES__STOP_SEQUENCE   = 4

#-stops's columns-#
STOPS__STOP_ID              = 0
STOPS__STOP_CODE            = 1
STOPS__STOP_NAME            = 2 
STOPS__STOP_LAT             = 3 
STOPS__STOP_LON             = 4
STOPS__STOP_URL             = 5
STOPS__LOCATION_TYPE        = 6
STOPS__PARENT_STATION       = 7
STOPS__WEELCHAIR_BOARDING   = 8