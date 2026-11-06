def fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"

    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif gevoel >= 10 and gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"

def weerstation():
    temperaturen = []

    for dag in range(1, 8):

        temp = input("Wat is op dag " + str(dag) + " de temperatuur[C]: ")

        if temp == "":
            print("bye")
            break

        temp = float(temp)

        wind = float(input("Wat is op dag " + str(dag) + " de windsnelheid[m/s]: "))
        vocht = int(input("Wat is op dag " + str(dag) + " de vochtigheid[%]: "))

        temperaturen.append(temp)

        Fahrenheit = fahrenheit(temp)
        rapport = weerrapport(temp, wind, vocht)

        gemiddelde = sum(temperaturen) / len(temperaturen)

        print("Het is", temp, "C (", Fahrenheit, "F)")
        print(rapport)
        print("Gem. temp tot nu toe is", round(gemiddelde, 2))
        print("======================================")

weerstation()
