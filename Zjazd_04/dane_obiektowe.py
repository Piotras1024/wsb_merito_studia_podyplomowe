class CityAnalizer:
    def __init__(self, filename = 'dane.csv'):
        self.citys = {}
        self.filename = filename
        self.load_data()

    def load_data(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            first_line = file.readline()
            lines = file.readlines()

        data = [line.strip().split(',') for line in lines]

        for row in data:
            current_city = row[4]
            height = int(row[2])
            if current_city in self.citys:
                self.citys[current_city]['total'] += height
                self.citys[current_city]['number'] += 1
            else:
                self.citys[current_city] = {'total': height, 'number': 1}


    def show_height(self, x ):

        for city, data in self.citys.items():
            average = data['total'] / data['number']
            print(f"Średni wzrost w mieście {city} wynosi: {average:.{x}f}")


city_MM = CityAnalizer()
city_MM.show_height(1)