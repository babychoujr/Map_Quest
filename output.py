#Eric Chou 95408627
#PROJECT 3: : Ride Across the River
#output.py

import mapquest

def find_latlng_list(json_result: dict)-> str:
   #Finding the latitude and longitude from the JSON object
   latlng_list = []
   route_entry = json_result['route']
   locations = route_entry['locations']
   for site in locations:
       latlng_list.append(site['displayLatLng']['lat'])
       latlng_list.append(site['displayLatLng']['lng'])
   return latlng_list

class Steps:
    #Finding the route of between the locations
    def find_steps(self, json_result):
        print('DIRECTIONS')
        route_entry = json_result['route']
        legs_entry  = route_entry['legs']
        for item in legs_entry:
            for inside_item in item['maneuvers']:
                print(inside_item['narrative'])

class Total_Distance:
    #Finds the total distance between the locations
    def find_total_distance(self, json_result):
        route_entry = json_result['route']
        distance = route_entry['distance']
        print('TOTAL DISTANCE: ', round(distance), 'miles')
        print()

class Total_Time:
    #Finds the total time between the locations
    def find_total_time(self, json_result):
        route_entry = json_result['route']
        time = route_entry['time']
        print('TOTAL TIME:', int(round(time/60)), 'minutes')
        print()

class Lat_Long:
    #Finds the latitude and longitude of the locations
    def check_lng(self, lng):
        if lng > 0: direction_lng = 'E'
        elif lng <= 0: direction_lng = 'W'
        return direction_lng

    def check_lat(self, lat):
        if lat > 0: direction_lat = 'N'
        elif lat <= 0: direction_lat = 'S'
        return direction_lat

    def find_lat_long(self, json_result):
        print('LATLONGS')
        route_entry = json_result['route']
        locations = route_entry['locations']
        for site in locations:
            lat = site['displayLatLng']['lat']
            lng = site['displayLatLng']['lng']
            print("%4.2f" % lat, end = '')
            print(self.check_lat(lat), end = ' ')
            print("%4.2f" % lng, end = '')
            print(self.check_lng(lng))
        print()

class Elevation:
    #Finds the Elevation
    def find_elevation(self, json_result):
        print('ELEVATIONS')
        latlng_list = find_latlng_list(json_result)
        for i in range(0, len(latlng_list), 2):
            lat_lng_string = str(latlng_list[i]) + ',' + str(latlng_list[i+1])
            json_elevation = mapquest.get_result(mapquest.build_elevation_url(lat_lng_string))
            site_elevation = json_elevation['elevationProfile']
            for site in site_elevation:
                print((site['height']))
        print()

