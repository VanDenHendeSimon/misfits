def toon_leerlingen():
    leerlingen = [
        "Simon Van Den Hende",
        "Lucas Daele"
    ]

    print("Dit is een programma van ")
    for leerling in leerlingen:
        print("- %s" % leerling)
    print("\n")


def vraag_woord():
    return input("Geef een woord: ")


def draai_woord_om(woord):
    return woord[::-1]


def check_palindroom(woord, omgedraaid_woord):
    if woord == omgedraaid_woord:
        print("%s is een palindroom" % omgedraaid_woord)


def oefening_1():
    toon_leerlingen()
    woord = vraag_woord()

    omgedraaid_woord = draai_woord_om(woord)
    print(omgedraaid_woord)

    check_palindroom(woord, omgedraaid_woord)


def vraag_tijdseenheden():
    return int(input("Geef een tijdstip: "))


def oefening_2():
    toon_leerlingen()
    tijdstip = vraag_tijdseenheden()

    aantal_stappen = 0
    afstand_startpunt = 0

    stappen_naar_voor = 2
    stappen_naar_achter = 1

    for i in range(tijdstip):
        if i % 2 == 0:
            print("%s stappen naar voor" % stappen_naar_voor)
            aantal_stappen += stappen_naar_voor

            afstand_startpunt += stappen_naar_voor

            stappen_naar_voor += 2
        else:
            print("%s stappen naar achter" % stappen_naar_achter)
            aantal_stappen += stappen_naar_achter

            afstand_startpunt -= stappen_naar_achter

            stappen_naar_achter += 1

    print("Afstand van het beginpunt: %s stappen" % afstand_startpunt)
    print("Hiervoor waren %s stappen nodig" % aantal_stappen)


# oefening_1()
oefening_2()
