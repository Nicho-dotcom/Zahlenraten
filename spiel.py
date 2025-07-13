import random
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