
station_dict = dict()
with open('station2.txt', 'r') as f:
    stations = f.read()
    for station in stations.split('\n'):
        if station.split(';')[0] == '':
            continue
        else:
            if station.split(';')[0] not in station_dict:
                station_dict[station.split(';')[0]] = list()
            station_dict[station.split(';')[0]].append(float(station.split(';')[1]))
    sorted_cities = sorted(station_dict)
    for city in sorted_cities:
        print(f'city: {city}, temp : AVG => {sum(station_dict[city])/len(station_dict[city])} ,'
                                  f' Min =>  {min(station_dict[city])},'
                                  f' Max =>  {max(station_dict[city])}')


# from collections import defaultdict
#
# station_dict = defaultdict(list)
#
# with open('station2.txt', 'r') as f:
#     for line in f:
#         if not line.strip():  # Skip empty lines
#             continue
#         city, temp = line.split(';')
#         if city:  # Ensure city name is not empty
#             station_dict[city].append(float(temp))
#
# sorted_cities = sorted(station_dict)
# for city in sorted_cities:
#     temps = station_dict[city]
#     avg_temp = sum(temps) / len(temps)
#     min_temp = min(temps)
#     max_temp = max(temps)
#     print(f'City: {city}, Temp: AVG => {avg_temp:.2f}, Min => {min_temp:.2f}, Max => {max_temp:.2f}')
