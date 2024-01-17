import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

class CityAnalizer:
    def __init__(self, filename='dane.csv'):
        self.dataframe = pd.read_csv(filename, sep=',', encoding='utf-8')
        self.dataframe.columns = ['id', 'age', 'height', 'weight', 'city']
        self.average_height_for_cities = self.dataframe.groupby('city')[['height', 'age', 'weight']].mean()

    def plot(self):
        ax = self.average_height_for_cities.plot(kind='bar', figsize=(15, 6))
        plt.title('Average Height for Cities', fontsize=15)
        plt.xlabel('Miasto')
        plt.ylabel('Średni wzrost w miastach')
        plt.xticks(rotation=0)

        for i in ax.patches:
            height = i.get_height()
            plt.annotate(f'{height:.2f}', xy=(i.get_x() + i.get_width() / 2, height),
                         textcoords='offset points', xytext=(0, -40), ha='center', rotation=90)

        # for i, value in enumerate(self.average_height_for_cities):
        #     plt.annotate(f'{value:.2f}', xy=(i, value), textcoords='offset points', xytext=(0, 5), ha='center')
        plt.show()
# .reset_index() -> aby pandas nie drukował tego ->> Name: age, dtype: float64

    def plot2(self):
        fig, ax1 = plt.subplots(figsize=(15, 6))
        self.average_height_for_cities['height'].plot(kind='bar', ax=ax1, color='blue', position=0, width=0.2)
        ax1.set_ylabel('Średni wzrost(cm)', color='blue')
        ax1.set_xlabel('Miasto', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')
        plt.xticks(rotation=0)

        ax2 = ax1.twinx()
        self.average_height_for_cities['weight'].plot(kind='bar', ax=ax2, color='red', position=1, width=0.2)
        ax2.set_ylabel('Średnia waga (kg)', color='red')
        ax2.tick_params(axis='y', labelcolor='red')

        plt.title('Średni wzrost i waga w miastach')
        plt.show()

    def plot_corr(self ):
        corr_matrix = self.dataframe[['height', 'age', 'weight']].corr()
        sns.heatmap(corr_matrix, annot=True)
        plt.show()

city = CityAnalizer()
city.plot_corr()
