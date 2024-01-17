import matplotlib.pyplot as plt

# Nazwy osób
names = ['tomek', 'adam', 'piotrek', 'Pasia']
# Wiek osób
ages = [15, 17, 30, 32]

# Stworzenie wykresu słupkowego
plt.figure(figsize=(8, 6))
plt.bar(names, ages)

# Dodanie tytułu i etykiet
plt.title('Wiek osób')
plt.xlabel('Imię')
plt.ylabel('Wiek')

# Ustawienie etykiet na osi X na nazwy osób
plt.xticks(ticks=range(len(names)), labels=names)

# Wyświetlenie wykresu
plt.show()
