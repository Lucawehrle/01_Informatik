def eingabeWerte(): 
    breite = float(input("Breite des Raumes (m):"))
    laenge = float(input("Länge des Raumes (m):"))
    hoehe = float(input("Höhe des Raums (m):"))
    t_innen = float(input("Innentemperatur (Grad Celsius):"))
    t_aussen = float(input("Außentemperatur (Grad Celsius):"))

    volumen = breite * laenge * hoehe 
    dt = t_innen - t_aussen
    return volumen,dt 

def berechneteHeizleistung(volumen,dt):
    ergebnis = volumen * dt * 0.024
    return ergebnis

volumen,dt = eingabeWerte()
if dt < 0:
    print(f"Achtung Temperaturdifferenz zu klein {dt} < 0")

heizleistung = berechneteHeizleistung(volumen,dt) 
print (f"heizleistung beträgt {heizleistung}kw")