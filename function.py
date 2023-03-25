def parameters(location):
    size = location["boundedBy"]["Envelope"]
    # Координаты центра топонима:
    center = location["Point"]["pos"]
    # Долгота и широта:
    long, lat = center.split(" ")
    upperl, upperla = int(size["upperCorner"].split()[0]), int(
        size["upperCorner"].split()[1])
    downl, downla = int(size["lowerCorner"].split()[0]), int(
        size["lowerCorner"].split()[1])
    up = round(upperl - downl, 3)
    flat = round(upperla - downla, 3)
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([long, lat]),
        "spn": ",".join([str(flat), str(up)]),
        "l": "map",
        "pt": ",".join([long, lat])
    }
    return map_params
