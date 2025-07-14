import random
def spiel_starten():
    while True:
        print("Lass uns ein Zahlenratespiel spielen.\nIch denke an eine Zahl zwischen 1 und deinem Schweregrad!")
        schwere = input("Möchtest du leicht(1-10), mittel(1-100) oder schwer(1-1000) spielen? (10/100/1000)")
        if not schwere.isdigit():
            print("Bitte gib nur eine der drei Zahlen ein!")
            continue
        schwere = int(schwere)
        if schwere not in [10,100,1000]:
            print("Bitte gib nur eine der drei genannten Zahlen ein!")
            continue
        else:
            break

    geheime_zahl = random.randint(1,schwere)
    print("Lass uns loslegen")
    print(f"Ich denke an eine Zahl zwischen 1 und {schwere}")
    versuche = 0
    while True:
        eingabe = input("Rate die Zahl: ")

        if not eingabe.isdigit():
            print("Probiers mit ner Zahl, Daggl!")
            continue
        tipp = int(eingabe)
        versuche +=1
        if tipp < geheime_zahl:
            print("Das war zu klein!")
        elif tipp > geheime_zahl:
            print("probiers mal kleiner")
        else:
            print(f"\nSuper, die Zahl war {geheime_zahl}.")
            print(f"du hast {versuche} Versuche gebraucht.")
            break
while True:
    spiel_starten()
    while True:
        nochmal = input("Magst du nochma? (j/n): ")
        if nochmal.lower() == "j":
            continue
        elif nochmal.lower() == "n":
            print("Danke fürs Dabeisein, bis bald")
            exit()
        else:
            print("Du solltest schon j für Ja oder n für Nein eintippen!")