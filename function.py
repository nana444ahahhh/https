def parameters(toponym):
    size = toponym["boundedBy"]["Envelope"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    upperl, upperla = float(size["upperCorner"].split()[0]), float(
        size["upperCorner"].split()[1])
    downl, downla = float(size["lowerCorner"].split()[0]), float(
        size["lowerCorner"].split()[1])
    up = round(upperl - downl, 3)
    flat = round(upperla - downla, 3)
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(flat), str(up)]),
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude])
    }
    return map_params
