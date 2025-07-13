import random
def spiel_starten():
    geheime_zahl = random.randint(1,100)
    print("Lass uns ein Spiel Spielen")
    print("Ich denke an eine Zahl zwischen 1 und 100")
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
            print(f"Super, die Zahl war {geheime_zahl}.")
            print(f"du hast {versuche} Versuche gebraucht.")
            break
while True:
    spiel_starten()
    nochmal = input("Magst du nochma? (j/n): ")
    if nochmal.lower() == "j":
        continue
    elif nochmal.lower() == "n":
        print("Danke fürs Dabeisein, bis bald")
        break
    else:
       nochmal = input("Wir können nur mit nem Ja oder Nein weitermachen (j/n)")