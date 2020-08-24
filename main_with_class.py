import requests
import datetime


def format_date(timestamp):
    """ Format a UNIX timestamp object to datetime format """

    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


class ISSClient:
    def __init__(self, req):
        if req == 'location':
            self.get_location()
        elif req == 'passover':
            self.get_passover()
        elif req == 'people':
            self.get_people()
        elif req == 'exit':
            exit()
        else:
            self.display_input()

    def get_location(self):
        """ Requests and prints current location """

        res = requests.get("http://api.open-notify.org/iss-now.json")
        data_location = res.json()

        unixtime_location = data_location["timestamp"]
        formatted_time_location = format_date(unixtime_location)
        location = str(data_location["iss_position"])

        print("The ISS current location at time: " + formatted_time_location + " is " + location)

    def get_passover(self):
        """ Requests and prints passover time for given latitude and longitude """

        latitude = float(input("Enter a latitude: "))
        longitude = float(input("Enter a longitude: "))
        parameters = {"lat": latitude, "lon": longitude}
        res = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters).json()

        overhead = res['response'][0]['risetime']
        time_overhead = format_date(overhead)

        print("The ISS will be overhead at latitude: " + str(latitude) + " and longitude: " +
              str(longitude) + " at " + time_overhead)

    def get_people(self):
        """ Requests and prints names of people aboard the ISS """

        people = requests.get("http://api.open-notify.org/astros.json")
        data_people = people.json()
        names = [i['name'] for i in data_people['people']]
        formatted_names = ', '.join(str(x) for x in names)

        print(f'There are {len(names)} people aboard the ISS. Their names are: {formatted_names}')

    def display_input(self):
        """ Displays the valid inputs to the programs given an invalid input Exception """

        print("Invalid Input: You may enter: 'location', 'passover' or 'people'")


if __name__ == '__main__':
    while True:
        request = input("What would you like to know? You may enter: location, passover or people: ")
        t = ISSClient(request)
