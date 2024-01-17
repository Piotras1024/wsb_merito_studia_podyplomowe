import os
import time
import matplotlib.pyplot as plt


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

    @staticmethod
    def calculate_average(city_data):
        return city_data['total'] / city_data['number']

    def average_height(self, spec_city="", decimal_places=2):
        if spec_city:
            try:
                data = self.cities[spec_city]
                average = City_Analizer.calculate_average(data)
                print(f'W mieście {spec_city}: {average:.{decimal_places}f}')
            except KeyError:
                print(f"Nie ma takiego miasta {spec_city}.")
        else:
            for city, data in self.cities.items():
                average = City_Analizer.calculate_average(data)
                print(f'W mieście {city}: {average:.{decimal_places}f}')

    def average(self, decimal_places=2):
        averages = {}
        for city_name, data in self.cities.items():
            average_height = City_Analizer.calculate_average(data)
            averages[city_name] = round(average_height, decimal_places)
        return averages

    def show_cities(self, spec_city=""):
        if spec_city:
            print(f"Twoje miasto to {spec_city}")
        else:
            for city in self.cities.keys():
                print(city)

    def plot(self):
        averages = self.average()
        cities_name = list(averages.keys())
        values_data = list(averages.values())
        plt.figure(figsize=(10,6))
        plt.bar(cities_name, values_data)
        plt.title('Średni wzrost w różnych miastach')
        plt.xlabel("Miasto")
        plt.ylabel("Średni Wzrost")
        plt.show()


city = City_Analizer()
city.plot()
