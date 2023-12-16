with open('dane.csv', 'r', encoding='utf8') as file:
    first_line = file.readline()
    lines = file.readlines()

#print(first_line)
#print()
#print(lines)

data = [line.strip().split(',') for line in lines ]
average_high = sum(int(line[2]) for line in data) / len(data)

total_height = 0
i = 0


heights_city = {}
age_city = {}
weight_city = {}

for row in data:
    city = row[4]
    height = int(row[2])
    age = int(row[1])
    weight = int(row[3])

    if city not in heights_city:
        heights_city[city] = [height]
        weight_city[city] = [weight]
        age_city[city] = [age]
    else:
        heights_city[city].append(height)
        age_city[city].append(age)
        weight_city[city].append(weight)

for city in heights_city.keys():
    average_high = sum(heights_city[city])/len(heights_city[city])
    average_weight = sum(weight_city[city])/len(weight_city[city])
    average_age = sum(age_city[city])/len(age_city[city])
    print(city, "średni wzrost  w tym mieście to :", round(average_high, 2))
    print(city, "średni wiek  w tym mieście to :", round(average_age, 2))
    print(city, "średni waga  w tym mieście to :", round(average_weight, 2))


print(age_city["Warszawa"])


