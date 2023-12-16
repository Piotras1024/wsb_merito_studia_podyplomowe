with open('dane.csv', 'r', encoding='utf8') as file:
    first_line = file.readline()
    lines = file.readlines()

#print(first_line)
#print()
#print(lines)

data = [line.strip().split(',') for line in lines ]


average_high = sum(int(line[2]) for line in data) / len(data)
print(average_high)
