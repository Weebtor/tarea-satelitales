
# Autores: José Matamala, Víctor Sánchez
# Curso: Cominicaciones Satelitales
# Año: 2021

import numpy as np

option = 0
while(option != 2):
    print(  '\n'+"            Ingresar Opcion" +'\n')
    print("1.Determinar Datos (Angulo de elevacion - azimut - Visibilidad)")
    print("2.Terminar Programa")

    option=float(input('Opcion: '))

    if (option == 1):
        print('\n'+"            Ingresar Datos" +'\n')
        Latitud_e=float(input('LATITUD de la estacion terrena: '))
        longitud_e=float(input('LONGITUD de la estacion: '))
        Latitud_s=float(input('LATITUD del satelite: '))
        longitud_s=float(input('LONGITUD del  satelite: '))
        r_s= float(input('Altura del satelite(KM): '))

        r_s = r_s + 6371
        r_e = 6371

        if(Latitud_e <= 90 and Latitud_e >= -90 and Latitud_s < 1 and Latitud_s > -1 and longitud_e <= 180 and longitud_e >= -180 and longitud_s <= 180 and longitud_s >= -180 and r_s > 35700):
            
            print('\n'+"            RESULTADOS" +'\n')

            Latitud_e = np.deg2rad(Latitud_e)
            longitud_e = np.deg2rad(longitud_e)
            Latitud_s = np.deg2rad(Latitud_s)
            longitud_s = np.deg2rad(longitud_s)

            # Obtener Gamma
            cosGamma = np.cos(Latitud_e)*np.cos(Latitud_s)*np.cos(longitud_s - longitud_e) + np.sin(Latitud_e)*np.sin(Latitud_s)
            gamma = np.arccos(cosGamma)

            # Obtener angulo de elevacion
            cosEl = np.sin(gamma)/ np.sqrt((1 + np.power(r_e/r_s, 2) - 2*(r_e/r_s)*np.cos(gamma)))
            El = np.arccos(cosEl) if np.rad2deg(gamma) < 90 else -np.arccos(cosEl)
            print(f"---> Ángulo de elevación: {np.rad2deg(El)}°")

            d = r_s* np.sqrt((1 + np.power(r_e/r_s, 2) - 2*(r_e/r_s)*np.cos(gamma)))
            a_intemedio = np.arctan((np.tan(np.abs(longitud_s - longitud_e)/np.sin(np.abs(Latitud_e)))))

            # Azimut

            Beta = longitud_s - longitud_e

            alpha = np.arctan((np.tan(np.abs(Beta)))/(np.sin(Latitud_e)))
            alphaD = np.rad2deg(alpha)

            if (alphaD > 0 ):
                alphaD = alphaD + 180
            if alphaD < 0 : #Pasarlos a positivo
                 alphaD = alphaD + 360

            if (Latitud_e < 0 and  Beta > 0 ):#subsatelite al noroeste
                Az = 360 - alphaD
                print ("---> Azimut: ",Az)
            elif (Latitud_e < 0 and Beta < 0 ): #subsatelite al noreste
                Az = alphaD
                print ("---> Azimut: ",Az)
            elif (Latitud_e > 0 and Beta < 0 ):#subsatelite al suroeste
                Az = 180 + alphaD
                print ("---> Azimut: ",Az)
            elif (Latitud_e > 0 and Beta > 0 ):#subsatelite al sureste
                Az = 180 - alphaD
                print ("---> Azimut: ",Az)


            #Visibilidad
            asd = r_e/cosGamma
            if El >= 0 and r_s >= asd:
                print(f"---> El satelite SI es visible")
            else:
                print(f"---> El satelite NO es visible")


        else:
            print('\n'+"Datos ingresados erroneos, favor intentelo denuevo...")
            print('\n'+"            ERRORES: " +'\n')
            if(Latitud_e > 90 or Latitud_e < -90 ):
                print("-> Latitud de la estacion terreste fuera de rango")
            if(Latitud_s > 1 or Latitud_s < -1 ):
                print("-> Latitud de del satelite Geostacionario debe ser cercana al ecuador")
            if(longitud_e > 180 or longitud_e < -180 ):
                print("-> Longitud de la estacion terreste fuera de rango")
            if(longitud_s > 180 or longitud_s < -180 ):
                print("-> Longitud del Satelite fuera de rango")
            if(r_s < 35700 ):
                print("-> La altura es menor que la de un satelite Geostacional")
            

