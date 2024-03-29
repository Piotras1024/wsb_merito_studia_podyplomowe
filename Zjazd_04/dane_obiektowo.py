import os
import time

class City_Analizer:
    def __init__(self, filename='dane.csv'):
        self.cities = {}
        self.filename = filename
        self.last_modified = 0
        self.load_data()

    def load_data(self):
        modification_time = os.path.getmtime(self.filename)
        if modification_time != self.last_modified:
            self.last_modified = modification_time
            self.cities.clear()
            with open(self.filename, 'r', encoding='utf-8') as file:
                first_line = file.readline()
                lines = file.readlines()
            data = [line.strip().split(',') for line in lines]
            for row in data:
                city = row[4]
                height = int(row[2])
                if city in self.cities:
                    self.cities[city]['total'] += height
                    self.cities[city]['number'] += 1
                else:
                    self.cities[city] = {'total': height, 'number': 1}

    def average_height(self, spec_city="", decimal_places=2):

        def calculate_average(city_data):
            return city_data['total'] / city_data['number']

        if spec_city:
            try:
                average = calculate_average(self.cities[spec_city])
                print(f'W mieście {spec_city}: {average:.{decimal_places}f}')
            except KeyError:
                print(f"Nie ma takiego miasta {spec_city}.")
        else:
            for city, data in self.cities.items():
                average = calculate_average(data)
                print(f'W mieście {city}: {average:.{decimal_places}f}')

    def show_cities(self, spec_city=""):
        if spec_city:
            print(f"Twoje miasto to {spec_city}")
        else:
            for city in self.cities.keys():
                print(city)


def main():
    cities_data = City_Analizer()
    while True:
        choose = input("Podaj miasto ( 'exit' ) aby wyjść").capitalize()
        cities_data.load_data()
        if choose.lower() == "exit":
            print('Narazie')
            break
        elif choose == "":
            cities_data.show_cities(choose)
            cities_data.average_height(choose)
        elif choose not in cities_data.cities.keys():
            print(f"{choose} - > Nie ma takiego miasta w bazie danych, spróbuj jeszcze raz !")
        else:
            print(f"Twoje miasto to {choose} !!!")
            cities_data.average_height(choose)



if __name__ == "__main__":
    main()
