def aantal_dagen(inputFile):
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()
    return len(regels) - 1
    #telt regels en haalt eentje af, eerste regel bevat kolomnamen

def auto_bereken(inputFile, outputFile):
    invoer = open(inputFile, "r")
    regels = invoer.readlines()
    invoer.close()
    uitvoer = open(outputFile, "w")
    #leest input "r" en schrijft "w" resultaten in output

    for regel in regels[1:]: #slaat eerste regel over
        datum, personen, setpoint, buiten, regen = regel.split()
        verschil = float(setpoint) - float(buiten)
        #temp verschil berekent
        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = min(int(personen) + 1, 4)
        #min zorgt dat de uitkomst noot hoger is dan 4
        bewatering = float(regen) < 3
        #aan bij minder dan 3mm
        uitvoer.write(
            f"{datum};{cv};{ventilatie};{bewatering}\n")
            #waardes gescheiden door puntkommas en \n zorgt voor nieuwe regels per dag
    uitvoer.close()

def overwrite_settings(outputFile):
    datum = input("Datum: ")
    systeem = input("Systeem (1=CV, 2=Ventilatie, 3=Bewatering): ")
    waarde = input("Nieuwe waarde: ")
    #hier kun je drie dingen aanpassen voor een van de dagen
    bestand = open(outputFile, "r")
    regels = bestand.readlines()
    #leest alle regels om de juiste datum te vinden en aanpassen
    bestand.close()

    for i in range(len(regels)): #loopt langs alle regels en scheidt ze met puntkomma
        gegevens = regels[i].strip().split(";")

        if gegevens[0] == datum: #code kijkt welke keuze je gemaakt hebt
            if systeem == "1" and waarde.isdigit() and int(waarde) <= 100: #waarde kan niet groter dan 100
                gegevens[1] = waarde
            elif systeem == "2" and waarde.isdigit() and int(waarde) <= 4: #waarde kan niet groter dan 4
                gegevens[2] = waarde
            elif systeem == "3" and waarde in ["0", "1"]: #waarde moet 0 of 1, false/true
                gegevens[3] = str(waarde == "1")
            else:
                print("Ongeldige invoer!")
                return -3

            regels[i] = ";".join(gegevens) + "\n" #zet aanpassingen achter elkaar met puntkommas
            bestand = open(outputFile, "w")
            bestand.writelines(regels) #schrijft alle regels terug naar output
            bestand.close()
            print("Waarde aangepast!")
            return 0

    print("Datum niet gevonden!")
    return -1

def smart_app_controller():
    while True:
        print("\n1. Aantal dagen\n2. Berekenen\n3. Overschrijven\n4. Stoppen")
        #zorgt ervoor dat het menu steeds opnieuw verschijnt
        keuze = input("Kies: ")
        #programma vraagt jouw keuze
        if keuze == "1":
            print("Aantal dagen:", aantal_dagen("input.txt"))
        elif keuze == "2":
            auto_bereken("input.txt", "output.txt")
            print("Output gemaakt!")
        elif keuze == "3":
            overwrite_settings("output.txt")
        elif keuze == "4":
            break
        else:
            print("Ongeldige keuze!")

smart_app_controller()