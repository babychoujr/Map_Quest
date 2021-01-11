#Eric Chou
#PROJECT 3
#input.py


#PRACTICE INPUTS
#4533 Campus Dr, Irvine, CA
#1111 Figueroa St, Los Angeles, CA
#3799 S Las Vegas Blvd, Las Vegas, NV

import output
import mapquest

def total_distance(result: dict)-> None:
    '''Creates an object and then uses the function in the Class to print out the total distance between the locations'''
    d = output.Total_Distance()
    d.find_total_distance(result)

def total_time(result: dict)-> None:
    '''Creates an object and then uses the function in the Class to print out the total time between the locations'''
    t = output.Total_Time()
    t.find_total_time(result)

def steps(result: dict)-> None:
    '''Creates an object and then uses the function in the Class to print out the directions between the locations'''
    s = output.Steps()
    s.find_steps(result)
    print()

def elevation(result: dict)-> None:
    '''Creates an object and then uses the function in the Class to print out the elevation between the locations'''
    e = output.Elevation()
    e.find_elevation(result)

def lat_long(result: dict)-> None:
    '''Creates an object and then uses the function in the Class to print out the lat and long of the locations'''
    lat_long = output.Lat_Long()
    lat_long.find_lat_long(result)

def location_info(line: int)-> list:
    '''finds the info types of the locations'''
    done = False
    while not done:
        try:
            list_of_outputs = []
            for i in range(line):
                output = input('Please write the type of output you would like?(STEPS, TOTALDISTANCE, TOTALTIME, LATLONG, OR ELEVATION): ')
                if output != output.upper():
                    raise ValueError()
                list_of_outputs.append(output)
            done = True
            return list_of_outputs
        except ValueError:
            print('Please try again(It must be uppercase and no extra whitespaces)')

def check_line()-> int:
    '''Checks if the number of outputs generated entered is greater than 1'''
    done = False
    while not done:
        try:
            line = int(input('Please the number of outputs generated: '))
        except TypeError:
            print('Please enter an integer that is greater or equal to 1.')
        else:
            if line >= 1:
                return line
            else:
                print('Please enter a number that is greater or equal to 1.')

def check_locations()-> None:
    '''Checks if the number of locations entered is greater than 2'''
    done = False
    while not done:
        try:
            numb_locations = int(input('Please enter the number of locations: '))
        except TypeError:
            print('Please enter an integer that is greater or equal to 2')
        else:
            if numb_locations >= 2:
                return numb_locations
            else:
                print('Please enter a number that is greater or equal to 2')

def find_locations(numb_locations: int)-> list:
    '''finds the locations entered and puts it into a list'''
    done = False
    while not done:
        try:
            list_of_locations = []
            for i in range(numb_locations):
                mapquest_location = input('Please describe your location: ')
                list_of_locations.append(mapquest_location)
            done = True
            return list_of_locations
        except:
            pass

def print_user_input(features: list, result: dict)-> None:
    '''Prints out the feature of the location depending on what the user typed in '''
    for i in range(len(features)):
        if features[i] == 'STEPS':
            steps(result)
        elif features[i] == 'TOTALDISTANCE':
            total_distance(result)
        elif features[i] == 'TOTALTIME':
            total_time(result)
        elif features[i] == 'LATLONG':
            lat_long(result)
        elif features[i] == 'ELEVATION':
            elevation(result)


def main():
    numb = check_locations()#checks the number of locations
    locations = find_locations(numb)#gets the locations and puts it in a list
    result = mapquest.get_result(mapquest.build_route_url(locations))#creates the dictionary
    checkoutput = check_line()# checks the number of outputs
    features = location_info(checkoutput)#asks the user for the outputs
    print()
    print_user_input(features, result)
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')



if __name__ == '__main__':
    main()
