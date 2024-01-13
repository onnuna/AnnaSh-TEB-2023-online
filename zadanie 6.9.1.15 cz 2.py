import errno
import os

class FileError(Exception):
    pass

class LineError(Exception):
    pass

class EmptyFileError(Exception):
    pass

def otworz():
    zrodlo = "C:/Users/SzczepanikTomasz/OneDrive - TEB tszczepanik/OneDrive - Grupa TEB Edukacja/Pulpit/"
    nazwa = "testfile.txt"
    try:
        strumien = open(zrodlo + nazwa, "r", encoding="utf-8")
        tekst = strumien.read()
        strumien.close()
        if not tekst:
            raise EmptyFileError("Plik jest pusty.")
        return tekst
    except FileNotFoundError:
        raise FileError("Plik nie istnieje.")
    except Exception as exc:
        raise exc

def main():
    try:
        tekst = otworz()
        lst = []
        for line in tekst.split("\n"):
            parts = line.split()
            if len(parts) != 3:
                raise LineError(f"Nieprawidłowa linia: {line.strip()}")
            
            name = parts[0] + ' ' + parts[1]
            score = float(parts[2])
            
            found = False
            for item in lst:
                if item[0] == name:
                    item[1] += score
                    found = True
                    break
            
            if not found:
                lst.append([name, score])
        
        lst.sort(key=lambda x: x[1], reverse=True)
        for item in lst:
            print(item[0], item[1])
            
    except FileError as fe:
        print(fe)
    except LineError as le:
        print(le)
    except EmptyFileError as efe:
        print(efe)
    except Exception as e:
        if hasattr(e, 'errno'):
            if e.errno == errno.ENOENT:
                print("Plik nie istnieje.")
            elif e.errno == errno.EMFILE:
                print("Otworzyles zbyt wiele plikow.")
        else:
            print("Numer bledu to:", e)

if __name__ == "__main__":
    main()