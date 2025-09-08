import datetime as dt

fajl_nev = "elelmiszerek.csv"

def fajl_betoltese(fajlnev):
    with open(fajlnev, "r", encoding="UTF-8") as f:
        sorok = f.readlines()
    del sorok[0]
    adatok = []
    for s in sorok:
        line = s.strip().split(";")
        line[5] = dt.datetime.strptime(line[5],"%Y.%m.%d")
        line[1] = float(line[1])
        line[2] = float(line[2])
        line[3] = float(line[3])
        adatok.append(line)
    return adatok


def kaloria_szamito(feherje, zsir, szenhidrat):
    return feherje * 4 + zsir * 8 + szenhidrat * 8

def kategoria_listazas(elelmiszerek):
    kategoriak = []
    for i in range(0, len(elelmiszerek)):
        if elelmiszerek[i][4] not in kategoriak:
            kategoriak.append(elelmiszerek[i][4])
    print(kategoriak)
    valasztott_kategoria = input("Kérem, adjon meg egy kategóriát: ")
    if valasztott_kategoria not in kategoriak:
        return "A választott kategróia nem létezik!"
    kiirando = []
    with open("eredmenyek.txt", "w", encoding="UTF-8") as e:
        for i in range(0, len(elelmiszerek)):
            if elelmiszerek[i][4] == valasztott_kategoria:
                lines = f"{elelmiszerek[i][0]};{kaloria_szamito(elelmiszerek[i][1],elelmiszerek[i][2],elelmiszerek[i][3])}"
                kiirando.append(lines)
        e.write("\n".join(kiirando))
    return "A fájlba írás befejeződött!"

elelmiszerek = fajl_betoltese(fajl_nev)

while True:
    menu = input("********FŐMENÜ*******************\n(K) Adott kategória élelmiszereinek listázása\n(Q) Kilépés\nKérem, adjon meg egy parancsot: ")
    if menu.lower() == "k":
        print(kategoria_listazas(elelmiszerek))
    elif menu.lower() == "q":
        break