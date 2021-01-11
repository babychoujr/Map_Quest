import mapquest

class Steps:
    '''Finding the route of between the locations'''
    def find_steps(self, json_result):
            print('STEPS')
            top = json_result['route']['legs']
            for item in (top):
                for inside_item in item['maneuvers']:
                    print(inside_item['narrative'])

class Total_Distance:
    '''Finds the total distance between the locations'''
    def find_total_distance(self, json_result):
            distance = json_result['route']['distance']
            print('TOTAL DISTANCE:', distance, 'miles')
            print()

class Total_Time:
    '''Finds the total time between the locations'''
    def find_total_time(self, json_result):
            time = json_result['route']['time']
            print('TOTAL TIME:', int(round(time/60)), 'minutes')
            print()

class Lat_Long:
    '''Finds the latitude and longitude of the locations'''
    def check_lng(self, lng):
        if lng > 0:
            direction_lng = 'E'
        elif lng <= 0:
            direction_lng = 'W'
        return direction_lng

    def check_lat(self, lat):
        if lat > 0:
            direction_lat = 'N'
        elif lat <= 0:
            direction_lat = 'S'
        return direction_lat

    def find_lat_long(self, json_result):
            print('LATLONGS')
            top = json_result['route']['locations']
            for i in top:
                #lng = i['displayLatLng']['lng']
                lat = i['displayLatLng']['lat']
                lng = i['displayLatLng']['lng']
                print(round(lat, 2), end = '')
                print(self.check_lat(lat), end = ' ')
                print(round(lng, 2), end = '')
                print(self.check_lng(lng))
            print()

class Elevation:
    '''Finds the Elevation'''
    def find_elevation(self, json_result):
        print('ELEVATION')
        latlng_list = find_latlng_list(json_result)
        for i in range(0, len(latlng_list), 2):
            lat_lng_string = str(latlng_list[i]) + ',' + str(latlng_list[i+1])
            json_elevation = mapquest.get_result(mapquest.build_elevation_url(lat_lng_string))
            top = json_elevation['elevationProfile']
            for j in top:
                print((j['height']))
        print()

def find_latlng_list(json_result: dict)-> str:
   latlng_list = []
   top = json_result['route']['locations']
   for i in top:
       latlng_list.append(i['displayLatLng']['lat'])
       latlng_list.append(i['displayLatLng']['lng'])
   return latlng_list