# Desarrolle un programa (Python, C/C++, Matlab) que al ingresar la ubicación de
# una estación terrena (latitud y longitud), 
# la ubicación de un satélite GEO (latitud y longitud) y la altura del satélite, 
# determine el ángulo de elevación, el Azimut y validar si hay o no visibilidad.

import numpy as np
Latitud_e = -33.42628  # latitud estación terrena
longitud_e = -70.56656 # longitud estación terrena
r_e = 6371 # altura estacion terrestre
Latitud_s = -0.03 # latitud satélite
longitud_s = 30.93 # longitud satélite
r_s = 35781.41 + r_e # altura del satelite

if __name__ == "__main__":

    Latitud_e = np.deg2rad(Latitud_e)
    longitud_e = np.deg2rad(longitud_e)
    Latitud_s = np.deg2rad(Latitud_s)
    longitud_s = np.deg2rad(longitud_s)


    # Obtener Gamma
    cosGamma = np.cos(Latitud_e)*np.cos(Latitud_s)*np.cos(longitud_s - longitud_e) + np.sin(Latitud_e)*np.sin(Latitud_s)
    gamma = np.arccos(cosGamma)
    print(f"COS(gamma): {cosGamma}")
    print(f"gamma: {np.rad2deg(gamma)}°")
    
    # Obtener angulo de elevacion

    cosEl = np.sin(gamma)/ np.sqrt((1 + np.power(r_e/r_s, 2) - 2*(r_e/r_s)*np.cos(gamma)))
    El = np.arccos(cosEl)

    print(f"ángulo de elevación: {np.rad2deg(El)}°")

    d = r_s* np.sqrt((1 + np.power(r_e/r_s, 2) - 2*(r_e/r_s)*np.cos(gamma)))
    print(f"distancia: {d}")

    a_intemedio = np.arctan((np.tan(np.abs(longitud_s - longitud_e)/np.sin(np.abs(Latitud_e)))))
    print(f"angulo intermedio: {np.rad2deg(a_intemedio)}")

    # falta determinar el azimut
    