import pandas as pd
from matplotlib import pyplot as plt


class CityAnalizer:
    def __init__(self, filename='dane.csv'):
        self.dataframe = pd.read_csv(filename, sep=',', encoding='utf-8')
        self.dataframe.columns = ['id', 'age', 'height', 'weight', 'city']
        # Dodanie .reset_index() do przechowywania miast jako kolumny
        self.average_height_for_cities = self.dataframe.groupby('city')['height'].mean().reset_index()

    def plot(self):
        # Tworzenie wykresu słupkowego
        self.average_height_for_cities.plot(kind='bar', x='city', y='height', figsize=(10, 6))
        plt.title('Average Height for Cities', fontsize=15)
        plt.xlabel('Miasto')
        plt.ylabel('Średni wzrost w miastach')
        plt.xticks(rotation=45)

        # Dodanie adnotacji
        # for index, row in self.average_height_for_cities.iterrows():
        #     plt.annotate(f'{row["height"]:.2f}', xy=(index, row['height']), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')

        plt.show()

city = CityAnalizer()
city.plot()
