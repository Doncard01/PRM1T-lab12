import funkcje, sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise AssertionError("Podaj dokładnie jeden argument wywołania pliku!")
    try:
        funkcje.Funkcja2(sys.argv[1])
    except (AssertionError, FileExistsError) as err:
        print(f"Błąd: {err}")