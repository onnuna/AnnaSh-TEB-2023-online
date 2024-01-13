import errno, os

def znajdz(lst, litera):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == litera.upper():
                return i

def otworz():
    zrodlo = "C:/Users/SzczepanikTomasz/OneDrive - TEB tszczepanik/OneDrive - Grupa TEB Edukacja/Pulpit/"
    nazwa = "testfile.txt"
    strumien = open(zrodlo + nazwa, "r", encoding="utf-8")
    tekst = strumien.read()
    strumien.close()
    return tekst

try:
    tekst = otworz()
    lst = []
    for i in tekst:
        if i.isalpha():
            idx = znajdz(lst, i)
            if idx is not None:
                lst[idx][1] = lst[idx][1] + 1
            else:
                lst.append([i.upper(), 1])
    lst.sort(key=lambda x: x[1], reverse=True)
    with open("samplefile.hist", "w") as f:
        for i in range(len(lst)):
            f.write(f"{lst[i][0]} -> {lst[i][1]}\n")
        print("Histogram został zapisany do pliku samplefile.hist.")

except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("Plik nie istnieje.")
    elif exc.errno == errno.EMFILE:
        print("Otworzyles zbyt wiele plikow.")
    else:
        print("Numer bledu to:", exc.errno)