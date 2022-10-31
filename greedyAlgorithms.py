states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# comment
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed: 
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items(): # states_for_station = названия штатов
     covered = states_needed & states_for_station # множество штатов, не входящих в покрытие, которые покрываются текущей станцией
     if len(covered) > len(states_covered): # покрывает ли эта станция больше штатов, чем текущая 
        best_station = station
        states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)