# Koordináta bekérése
elso_koordinata_input = input("Add meg a koordinátát az elsőhöz (x, y formátumban): ")

# Szöveg feldolgozása
x, y = map(int, elso_koordinata_input.strip("()").split(","))
print(f"A megadott koordináta: x = {x}, y = {y}")

# Koordináta bekérése
elso_koordinata_input2 = input("Add meg a koordinátát a másodikhoz (x, y formátumban): ")

# Szöveg feldolgozása
x2, y2 = map(int, elso_koordinata_input2.strip("()").split(","))
print(f"A megadott koordináta: x = {x2}, y = {y2}")


# Két pont koordinátái
elso_x = x
elso_y = y
masodik_x = x2
masodik_y = y2

# Meredekség (m) kiszámítása
m = (masodik_y - elso_y) / (masodik_x - elso_x)

# Y-tengelymetszet (b) kiszámítása
b = elso_y - m * elso_x

# Az egyenes egyenlete: y = mx + b
print(f"Az egyenes egyenlete: y = {m}x + {b}")

# Kétpont-forma
print(f"Az egyenes kétpont-formája: y - {elso_y} = {(masodik_y - elso_y) / (masodik_x - elso_x)}(x - {elso_x})")

###########################################################################################################################################################

masodik_koordinata_input = input("Add meg a koordinátát a harmadikhoz (x, y formátumban): ")

x3, y3 = map(int, masodik_koordinata_input.strip("()").split(","))
print(f"A megadott koorináta: x = {x3}, y = {y3}")

# Adott pontok
harmadik_x = x3
harmadik_y = y3


# Merőleges egyenes meredeksége (m_perpendicular)
if m != 0:  # Ha az eredeti egyenes nem függőleges
    m_perpendicular = -1 / m
else:  # Ha az eredeti egyenes vízszintes
    m_perpendicular = float('inf')  # Függőleges lesz

# Merőleges egyenes tengelymetszete (b_perpendicular)
if m_perpendicular != float('inf'):  # Ha nem függőleges
    b_perpendicular = harmadik_y - m_perpendicular * harmadik_x

    # Merőleges egyenes egyenlete
    print(f"A merőleges egyenes: y = {m_perpendicular}x + {b_perpendicular}")
else:
    # Ha a merőleges függőleges
    print(f"A merőleges egyenes: x = {harmadik_x}")










