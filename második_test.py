import numpy as np
import elso_fajl

# Adott pontok
x1, y1 = elso_fajl.elso_x, elso_fajl.elso_y
x2, y2 = elso_fajl.masodik_x, elso_fajl.masodik_y
x3, y3 = elso_fajl.harmadik_x, elso_fajl.harmadik_y

# Eredeti egyenes meredeksége
m = (y2 - y1) / (x2 - x1)

# Merőleges egyenes meredeksége
m_perpendicular = -1 / m

# Merőleges egyenes tengelymetszete
b_perpendicular = y3 - m_perpendicular * x3

# Bounding box határok (pl. [0, 10] intervallum mindkét tengelyen)
x_min, x_max = 0, 1000
y_min, y_max = 0, 1000

# Függvény a metszéspontok kiszámítására
def find_intersection(m, b, x_min, x_max, y_min, y_max):
    points = []
    # Ellenőrizzük az y = y_min és y = y_max metszéspontokat
    for y in [y_min, y_max]:
        x = (y - b) / m
        if x_min <= x <= x_max:
            points.append((x, y))
    # Ellenőrizzük az x = x_min és x = x_max metszéspontokat
    for x in [x_min, x_max]:
        y = m * x + b
        if y_min <= y <= y_max:
            points.append((x, y))
    return points

# Metszéspontok számítása
endpoints = find_intersection(m_perpendicular, b_perpendicular, x_min, x_max, y_min, y_max)

# Eredmény kiíratása
print(f"A merőleges egyenes végpontjai: {endpoints}")















