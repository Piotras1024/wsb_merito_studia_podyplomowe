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

for row in data:
    city = row[4]
    height = int(row[2])

    if city not in heights_city:
        heights_city[city] = [height]
    else:
        heights_city[city].append(height)

for city in heights_city.keys():
    average_high = sum(heights_city[city])/len(heights_city[city])
    print(city, "średni wzrosty  w tym mieście to :", average_high)




